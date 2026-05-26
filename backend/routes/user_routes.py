from fastapi import APIRouter
from backend.database.db import SessionLocal
from backend.model.user import User

router = APIRouter()

@router.post("/register")
def register(name: str, email: str):

    db = SessionLocal()

    existing_user = db.query(User).filter(User.email == email).first()

    if existing_user:
        return {
            "message": "Email already registered"
        }

    user = User(name=name, email=email)

    db.add(user)
    db.commit()

    return {
        "message": "User Registered Successfully"
    }
@router.get("/users")
def get_users():

    db = SessionLocal()

    users = db.query(User).all()

    return users
@router.post("/login")
def login(email: str):

    db = SessionLocal()

    user = db.query(User).filter(User.email == email).first()

    if not user:
        return {"message": "User not found"}

    return {
        "message": "Login Successful",
        "user_id": user.id,
        "name": user.name
    }