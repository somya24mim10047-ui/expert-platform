from fastapi import FastAPI

from backend.database.db import Base, engine

from backend.model.user import User
from backend.model.wallet import Wallet
from backend.database.db import Base, engine

from backend.model.expert import Expert
from backend.model.call import Call

from backend.routes.user_routes import router
from backend.routes.expert_routes import router as expert_router
from backend.routes.wallet_routes import router as wallet_router
from backend.routes.call_routes import router as call_router
from backend.routes.redis_routes import router as redis_router
from backend.routes.auth_routes import router as auth_router
from backend.routes.webrtc_routes import router as webrtc_router
from backend.routes.availability_routes import router as availability_router
from backend.routes.pubsub_routes import router as pubsub_router
from backend.routes.billing_routes import router as billing_router
from backend.routes.cloudinary_routes import router as cloudinary_router
from backend.routes.appointment_routes import router as appointment_router
# Create tables
Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(router)
app.include_router(expert_router)
app.include_router(wallet_router)
app.include_router(call_router)
app.include_router(redis_router)
app.include_router(auth_router)
app.include_router(webrtc_router)
app.include_router(availability_router)
app.include_router(pubsub_router)
app.include_router(billing_router)
app.include_router(cloudinary_router)
app.include_router(appointment_router)

@app.get("/")
def home():
    return {"message": "Backend Running Successfully"}