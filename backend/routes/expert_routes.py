from fastapi import APIRouter
from backend.database.db import SessionLocal
from backend.model.expert import Expert

router = APIRouter()

@router.post("/expert")
def add_expert(name: str, specialization: str, price_per_minute: int):

    db = SessionLocal()

    expert = Expert(
        name=name,
        specialization=specialization,
        price_per_minute=price_per_minute
    )

    db.add(expert)
    db.commit()

    return {"message": "Expert Added"}
@router.get("/experts")
def get_experts():

    db = SessionLocal()

    experts = db.query(Expert).all()

    return experts