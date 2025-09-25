from fastapi import FastAPI, HTTPException
from sqlmodel import SQLModel

app = FastAPI()

# Usuario en memoria (aqui pudiera agregar una base de datos)
class User(SQLModel):
    username: str
    password: str

# Credenciales quemadas en código
admin_user = User(username="naruto", password="rasengan123")

class Credentials(SQLModel):
    username: str
    password: str

@app.get("/")
def index():
    return {"message": "Hola, darling, has ingresado correctamente"}

@app.post("/login")
def login(credentials: Credentials):
    if credentials.username == admin_user.username and credentials.password == admin_user.password:
        return {"message": f"¡Bienvenido, darling :)❤️ {admin_user.username}! Tu chakra está listo ⚡️"}
    raise HTTPException(401, "Usuario o contraseña incorrectos, revisa o contactate con el admin")
