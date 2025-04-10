from datetime import datetime, timedelta, timezone
import jwt

from token_data import TokenData


class TokenData(BaseModel):
    username: str
    exp_datetime: datetime


SECRET_KEY = "5ad79cf900c62688a9f066e7072ff50cb5160a0a93d1246da3bf095019e7c08d"
ALGORITHM = "HS256"


def create_access_token(data: dict, expires_delta: timedelta = timedelta(minutes=15)):
    payload = data.copy()
    expire = datetime.now(timezone.utc) + expires_delta
    payload.update({"exp": expire})
    encoded = jwt.encode(payload, SECRET_KEY, algorithm=ALGORITHM)
    return encoded


def decode_jwt_token(token: str) -> TokenData | None:
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=ALGORITHM)
        username: str = payload.get("user_name")
        exp: int = payload.get("exp")
        return TokenData(
            {"username": username, "exp_datetime": datetime.fromtimestamp()}
        )
    except jwt.InvalidTokenError:
        print("Invalid JWT token.")
