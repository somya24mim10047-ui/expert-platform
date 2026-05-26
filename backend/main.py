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

# Create tables
Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(router)
app.include_router(expert_router)
app.include_router(wallet_router)
app.include_router(call_router)

@app.get("/")
def home():
    return {"message": "Backend Running Successfully"}