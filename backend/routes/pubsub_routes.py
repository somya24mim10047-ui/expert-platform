from fastapi import APIRouter
from backend.database.redis_db import redis_client

router = APIRouter()

@router.post("/publish")
def publish_message(message: str):

    redis_client.publish(
        "expert_channel",
        message
    )

    return {
        "message": "Published successfully"
    }