from fastapi import APIRouter
from backend.database.db import SessionLocal
from backend.model.call import Call
from backend.model.wallet import Wallet

router = APIRouter()

@router.post("/call")
def create_call(
    user_id: int,
    expert_id: int,
    duration: int,
    cost: int
):

    db = SessionLocal()

    wallet = db.query(Wallet).filter(
        Wallet.user_id == user_id
    ).first()

    if not wallet:
        return {"message": "Wallet not found"}

    if wallet.balance < cost:
        return {"message": "Insufficient balance"}

    wallet.balance -= cost

    call = Call(
        user_id=user_id,
        expert_id=expert_id,
        duration=duration,
        cost=cost
    )

    db.add(call)
    db.commit()

    return {
        "message": "Call Recorded Successfully",
        "remaining_balance": wallet.balance
    }
    return {"message": "Call Recorded Successfully"}
@router.get("/calls")
def get_calls():

    db = SessionLocal()

    calls = db.query(Call).all()

    return calls