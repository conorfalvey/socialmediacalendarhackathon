from app.database.base import Base
from uuid import uuid4
from sqlalchemy import Column, UUID, DateTime, String
from sqlalchemy.orm import relationship


class Posts(Base):
    __tablename__ = "posts"
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid4)
    delivery_time = Column(DateTime(timezone=False), nullable=False)
    text = Column(String(), nullable=False)
    frequency = Column(String, nullable=False)
    platform_id = relationship("Platforms")
    user_id = relationship("Users")
