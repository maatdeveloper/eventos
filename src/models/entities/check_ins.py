from src.models.settings.base import Base
from sqlalchemy import Column, String, DateTime, ForeignKey
from sqlalchemy.sql import func

class CheckIns(Base):
    __tablename__ = "check_ins"
    
    id = Column(String, primary_key=True)
    created_id = Column(DateTime, default=func.now())
    attendeeId = Column(String, ForeignKey("attendees.id"))


    def __repr__(self):
        return f"Events [attendeeId={self.attendeeId}]"
    
