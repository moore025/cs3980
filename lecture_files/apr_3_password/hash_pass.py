from passlib.context import CryptContext

pwd_context = CryptContext(schemes=["bcrypt"])


class HashPassword:
    def create_hash(self, password: str):
        return pwd_context.hash(password)

    def create_hash_with_salt(self, password: str, salt: str):
        return pwd_context.hash(password, salt=salt)

    def verify_hash(self, input_password: str, hashed_password: str):
        return pwd_context.verify(input_password, hashed_password)
