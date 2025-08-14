from sqlalchemy import Column, Integer, String, Date
from todo_manager.database import Base

class Todo(Base):
    __tablename__ = "todos"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(200), nullable=False)
    deadline = Column(Date, nullable=False)
    status = Column(String(20), nullable=False, default="pending")
