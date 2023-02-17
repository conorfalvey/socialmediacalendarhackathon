from app.database.base import Base
from uuid import uuid4
from sqlalchemy import Column, UUID, String, Integer
from sqlalchemy.orm import mapped_column


class Platforms(Base):
    __tablename__ = "platforms"
    id = mapped_column(UUID(as_uuid=True), primary_key=True, default=uuid4)
    name = Column(String(), nullable=False)
    char_limit = Column(Integer(), nullable=True)
