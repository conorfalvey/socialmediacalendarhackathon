from app.database.base import Base
from uuid import uuid4
from sqlalchemy import Column, UUID, DateTime, String
from sqlalchemy.orm import relationship


class Accounts(Base):
    __tablename__ = "accounts"
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid4)
    user_id = relationship("Users")
    username = Column(String(), nullable=False)
    token = Column(String(), nullable=False)
    email = Column(String(), nullable=False)
    platform_id = relationship("Platform")
