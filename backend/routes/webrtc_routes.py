from fastapi import APIRouter

router = APIRouter()

offers = {}

@router.post("/webrtc/offer")
def create_offer(call_id: str, offer: str):
    offers[call_id] = offer
    return {"message": "Offer stored"}

@router.get("/webrtc/offer")
def get_offer(call_id: str):
    return {"offer": offers.get(call_id)}