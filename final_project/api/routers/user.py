import logging
from typing import Annotated
from beanie import PydanticObjectId
from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from passlib.context import CryptContext

from auth.jwt_auth import (
    LoginResult,
    Token,
    TokenData,
    create_access_token,
    decode_jwt_token,
)
from models.user import User, UserRequest

in_memory_db = {}

pwd_context = CryptContext(schemes=["bcrypt"])


class HashPassword:
    def create_hash(self, password: str):
        return pwd_context.hash(password)

    def verify_hash(self, input_password: str, hashed_password: str):
        return pwd_context.verify(input_password, hashed_password)


oauth2_scheme = OAuth2PasswordBearer(tokenUrl="users/sign-in")
hash_password = HashPassword()


def get_user(token: Annotated[str, Depends(oauth2_scheme)]) -> TokenData:
    print(token)
    print("PRINTING Token")
    return decode_jwt_token(token)


user_router = APIRouter()
logger = logging.getLogger(__name__)


@user_router.post(
    "/signup"
)  # If user has already signed up, then make sure they can't sign up again
async def sign_up(user: UserRequest):
    existing_user = await User.find_one(User.username == user.username)

    if existing_user:
        raise HTTPException(status_code=400, detail="User already exists.")

    hashed_pwd = hash_password.create_hash(user.password)
    new_user = User(
        username=user.username, password=hashed_pwd, email=user.email, role="BasicUser"
    )  # Add parameters to username for final project i.e. no more than 100 characters, no special characters, etc.
    await new_user.create()
    logger.info(f"User with username = {new_user.username} created")
    return {"message": "User created successfully"}


@user_router.post("/sign-in")
async def login_for_access_token(
    form_data: Annotated[OAuth2PasswordRequestForm, Depends()],
) -> LoginResult:
    ## Authenticate user by verifying the user in DB
    username = form_data.username
    existing_user = await User.find_one(User.username == username)
    if not existing_user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Username or Password is invalid",
        )

    authenticated = hash_password.verify_hash(
        form_data.password, existing_user.password
    )
    if authenticated:
        access_token = create_access_token(
            {"username": username, "role": existing_user.role}
        )
        logger.info(f"{username} signed in")
        return LoginResult(
            access_token=access_token,
            username=existing_user.username,
            role=existing_user.role,
        )

    raise HTTPException(status_code=401, detail="Username or Password is invalid")


@user_router.get("")
async def get_all_users(user: Annotated[TokenData, Depends(get_user)]) -> list[User]:
    if not user or not user.username:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail=f"Please login.",
        )
    if user.role != "AdminUser":
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail=f"You don't have enough permissions for this action.",
        )
    logger.info(f"{user.username} retrieved all users")
    return await User.find_all().to_list()


@user_router.put("/{id}")
async def update_user_role(
    id: PydanticObjectId, user: Annotated[TokenData, Depends(get_user)]
) -> dict:  # check this line
    if not user or not user.username:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail=f"Please login.",
        )
    if user.role != "AdminUser":
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail=f"You don't have enough permissions for this action.",
        )
    affected_user = await User.get(id)
    if not affected_user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"The user with ID={id} is not found.",
        )

    if affected_user.role == "BasicUser":
        affected_user.role = "AdminUser"

    else:
        affected_user.role = "BasicUser"

    await affected_user.save()
    logger.info(f"{user.username} changed {affected_user.username}'s role")
    return {"newRole": affected_user.role}


@user_router.delete("/{id}")
async def delete_user(
    id: PydanticObjectId, user: Annotated[TokenData, Depends(get_user)]
) -> dict:
    delete_user = await User.get(id)
    if delete_user:
        logger.info(f"{user.username} deleted {delete_user.username}")
        await delete_user.delete()
        return {"message": f"The user with ID={id} has been deleted."}
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail=f"The user with ID={id} is not found.",
    )
