from passlib.context import CryptContext

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

plain = "admin"
hash_from_db = "$2b$12$A2gtrOHIGU3noAGlPD5ca.rsWgY5KB1tYlWrGpM07ytTxJdU/3tQu"

print(pwd_context.verify(plain, hash_from_db))