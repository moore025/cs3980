from fastapi import FastAPI, Depends, HTTPException
from typing import Annotated
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from auth import create_access_token, decode_jwt_token, TokenData, Token
from hash_pass import *

hash_password = HashPassword()

in_memory_db = [{"username": "hi", "password": "a"}]

app = FastAPI()
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")


def get_user(token: Annotated[str, Depends(oauth2_scheme)]) -> TokenData:
    return decode_jwt_token(token)


@app.post("/token")
async def login_for_access_token(
    form_data: Annotated[OAuth2PasswordRequestForm, Depends()]
) -> str:
    ## Authenticate user by verifying the user in DB
    username = form_data.username
    for u in in_memory_db:
        if u["username"] == username:
            print(u["password"])
            print(hash_password.create_hash("hi123"))
            authenticated = hash_password.verify_hash(form_data.password, u["password"])
            if authenticated:
                access_token = create_access_token({"username": username})
                return Token(access_token=access_token)
    return HTTPException(status_code=401, detail="Invalid username or password")


@app.get("/users/me")
async def read_my_user_name(user: Annotated[TokenData, Depends(get_user)]) -> TokenData:
    token = ""
    user = decode_jwt_token(token)
    return user
