from sqlalchemy import Column, Integer, String, ForeignKey
from backend.database.db import Base

class Appointment(Base):
    __tablename__ = "appointments"

    id = Column(Integer, primary_key=True, index=True)

    user_id = Column(Integer, ForeignKey("users.id"))

    expert_id = Column(Integer, ForeignKey("experts.id"))

    date = Column(String)

    time = Column(String)

    status = Column(String, default="Pending")