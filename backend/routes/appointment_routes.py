from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from backend.database.db import SessionLocal
from backend.model.appointment import Appointment

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/appointments")
def create_appointment(
    user_id: int,
    expert_id: int,
    date: str,
    time: str,
    db: Session = Depends(get_db)
):

    appointment = Appointment(
        user_id=user_id,
        expert_id=expert_id,
        date=date,
        time=time
    )

    db.add(appointment)
    db.commit()
    db.refresh(appointment)

    return appointment