from fastapi import FastAPI, Depends
from typing import Annotated

from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm

from token_data import TokenData
from auth import create_access_token, decode_jwt_token

app = FastAPI()
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")


def get_user(token: Annotated[str, Depends(oauth2_scheme)]) -> TokenData:
    return decode_jwt_token(token)


@app.post("/token")
async def login_for_access_token(
    form_data: Annotated[OAuth2PasswordRequestForm, Depends()]
) -> str:
    ## assume user is authenticated by username and password verification
    username = form_data.username
    return create_access_token({"username": username})


@app.get("/users/me")
async def read_my_user_name(user: Annotated[TokenData, Depends(get_user)]) -> TokenData:
    token = ""
    user = decode_jwt_token(token)
    return user
