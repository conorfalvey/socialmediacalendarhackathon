from app.database.base import Base
from uuid import uuid4
from sqlalchemy import Column, UUID, DateTime, String
from sqlalchemy.orm import relationship


class Posts(Base):
    __tablename__ = "posts"
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid4)
    delivery_time = Column(String(), nullable=False)
    text = Column(String(), nullable=False)
    post_hash = Column(String(), nullable=False)
    frequency = Column(String(), nullable=False)
    platform_id = Column(UUID(as_uuid=uuid4()), nullable=False)
    user_id = Column(UUID(as_uuid=uuid4()), nullable=False)
