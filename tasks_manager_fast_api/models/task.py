from sqlalchemy import Integer, String, func, DateTime, ForeignKey, Date
from sqlalchemy.orm import relationship
from sqlalchemy.testing.schema import Column
from .base import Base


class Task(Base):

    __tablename__ = "task"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, nullable=False, index=True)
    description = Column(String, nullable=False)
    date_start = Column(Date)
    date_end = Column(Date)
    status = Column(String, default=False)
    created_at = Column(DateTime(timezone=True), default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())

    user_id = Column(Integer, ForeignKey("user.id"))
    user = relationship('User', back_populates='tasks')

