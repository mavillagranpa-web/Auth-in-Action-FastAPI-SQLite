# primero esto pip install fastapi
# luego esto python -m uvicorn main:app --reload
# INFO:     Uvicorn running on http://127.0.0.1:8000 (Press CTRL+C to quit)
# al momento de ingresar la dirrecion colocar /docs
#Usar modelos de SQL mode

from fastapi import FastAPI, HTTPException
from sqlmodel import SQLModel, Field, create_engine, Session, select

app = FastAPI()
engine = create_engine("sqlite:///database.db")

class Usuario(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    username: str
    password: str

class LoginData(SQLModel):
    username: str
    password: str

@app.on_event("startup")
def iniciar():
    SQLModel.metadata.create_all(engine)
    with Session(engine) as session:
        if not session.exec(select(Usuario).where(Usuario.username == "naruto")).first():
            session.add(Usuario(username="naruto", password="rasengan123"))
            session.commit()

@app.get("/")
def index():
    return {"message": "Hola, darling"}

@app.post("/login")
def login(data: LoginData):
    with Session(engine) as session:
        usuario = session.exec(select(Usuario).where(Usuario.username == data.username)).first()
        if usuario and usuario.password == data.password:
            return {"message": f"¡Bienvenido, darling :)❤️ {usuario.username}! ⚡️"}
        raise HTTPException(401, "Usuario o contraseña incorrectos, revisa o contactate con el admin")
