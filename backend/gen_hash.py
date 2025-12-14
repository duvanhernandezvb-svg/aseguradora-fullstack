from passlib.context import CryptContext

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def truncate(password: str) -> str:
    return password[:72]

password = "admin"

hashed = pwd_context.hash(truncate(password))

print(hashed)


