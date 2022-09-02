from passlib.context import CryptContext

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


def hash(password: str):
    return pwd_context.hash(password)


def verify(plain_password:str, hashed_password: str):
    # pwd_context.verify generates the hash and compares it hashed password.
    # So we dont have to write the logic for it
    return pwd_context.verify(plain_password, hashed_password)