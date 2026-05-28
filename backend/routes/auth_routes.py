from fastapi import APIRouter
from firebase_admin import auth

router = APIRouter()

@router.post("/verify-token")
def verify_token(token: str):

    try:
        decoded_token = auth.verify_id_token(token)

        return {
            "uid": decoded_token["uid"],
            "email": decoded_token.get("email")
        }

    except Exception as e:
        return {"error": str(e)}