from fastapi import APIRouter
from backend.database.db import SessionLocal
from backend.model.wallet import Wallet

router = APIRouter()

@router.post("/wallet/add")
def add_money(user_id: int, amount: int):

    db = SessionLocal()

    wallet = db.query(Wallet).filter(
        Wallet.user_id == user_id
    ).first()

    if wallet:
        wallet.balance += amount
    else:
        wallet = Wallet(
            user_id=user_id,
            balance=amount
        )
        db.add(wallet)

    db.commit()

    return {"message": "Money Added Successfully"}
@router.get("/wallet")
def get_wallet(user_id: int):

    db = SessionLocal()

    wallet = db.query(Wallet).filter(
        Wallet.user_id == user_id
    ).first()

    if not wallet:
        return {"balance": 0}

    return {"balance": wallet.balance}