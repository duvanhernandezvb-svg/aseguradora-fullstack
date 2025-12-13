from passlib.context import CryptContext

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

password = "admin"

# Truncar a 72 caracteres si es necesario
password_trunc = password[:72]

hashed = pwd_context.hash(password_trunc)

print("Contraseña:", password_trunc)
print("Hash generado:", hashed)

