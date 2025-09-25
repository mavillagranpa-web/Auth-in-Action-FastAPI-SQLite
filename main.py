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
            return {"message": f"¡Bienvenido {usuario.username}! ⚡️"}
        raise HTTPException(401, "Credenciales incorrectas")
