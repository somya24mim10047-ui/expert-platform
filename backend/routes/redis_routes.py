# backend/routes/redis_routes.py

from fastapi import APIRouter
from backend.database.redis_db import redis_client

router = APIRouter()

@router.get("/redis-test")
def redis_test():
    redis_client.set("message", "Redis Connected")
    value = redis_client.get("message")
    return {"redis_value": value}
@router.post("/expert/online")
def set_online(expert_id: int):
    redis_client.set(f"expert:{expert_id}", "online")
    return {"message": "Expert is online"}

@router.post("/expert/offline")
def set_offline(expert_id: int):
    redis_client.set(f"expert:{expert_id}", "offline")
    return {"message": "Expert is offline"}

@router.get("/expert/status")
def get_status(expert_id: int):
    status = redis_client.get(f"expert:{expert_id}")
    return {"expert_id": expert_id, "status": status}