from sqlalchemy import Column, Integer, String, Boolean, DateTime
from src.infrastructure.database import Base
from datetime import datetime

class Todos(Base):
    __tablename__ = 'todos'
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String)
    description = Column(String)
    priority = Column(Integer)
    complete = Column(Boolean, default=False)
    created_at = Column(DateTime, default=datetime.now())
