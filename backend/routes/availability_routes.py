from fastapi import APIRouter
from backend.database.redis_db import redis_client

router = APIRouter()

@router.post("/expert/online")
def expert_online(expert_id: int):

    redis_client.set(
        f"expert:{expert_id}",
        "online"
    )

    return {"message": "Expert is online"}


@router.post("/expert/offline")
def expert_offline(expert_id: int):

    redis_client.set(
        f"expert:{expert_id}",
        "offline"
    )

    return {"message": "Expert is offline"}


@router.get("/expert/status/{expert_id}")
def expert_status(expert_id: int):

    status = redis_client.get(
        f"expert:{expert_id}"
    )

    if not status:
        status = "offline"

    return {
        "expert_id": expert_id,
        "status": status
    }