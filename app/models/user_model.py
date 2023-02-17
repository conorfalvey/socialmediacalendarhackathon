from app.database.base import Base
from uuid import uuid4
from sqlalchemy import Column, UUID, DateTime, String
from sqlalchemy.orm import relationship, mapped_column


class Users(Base):
    __tablename__ = "users"
    id = mapped_column(UUID(as_uuid=True), primary_key=True, default=uuid4)
    name = Column(String(), nullable=False)
    email = Column(String(), nullable=False)
    pass_hash = Column(String(), nullable=False)
    notification_time = Column(String, nullable=False)
