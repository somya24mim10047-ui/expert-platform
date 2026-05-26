from sqlalchemy import Column, Integer, String
from backend.model.user import Base

class Expert(Base):
    __tablename__ = "experts"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100))
    specialization = Column(String(100))
    price_per_minute = Column(Integer)