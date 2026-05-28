from sqlalchemy import Column, Integer
from backend.database.db import Base

class Call(Base):
    __tablename__ = "calls"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer)
    expert_id = Column(Integer)
    duration = Column(Integer)
    cost = Column(Integer)

