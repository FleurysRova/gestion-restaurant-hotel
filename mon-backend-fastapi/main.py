from fastapi import FastAPI, Depends, HTTPException, status
from sqlalchemy.orm import Session
from databse import SessionLocal  # corrige si besoin
from models import User
from schemas import UserLogin
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173", "http://localhost:3000"],  # virgule ajoutée ici
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.post("/login")
def login(data: UserLogin, db: Session = Depends(get_db)):
    user = db.query(User).filter(User.user_email == data.email).first()
    if not user or user.user_password != data.password:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Email ou mot de passe incorrect")
    return {"message": f"Connexion réussie, bienvenue {user.user_firstname}"}
