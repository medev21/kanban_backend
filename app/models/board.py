from .base_class import Base
from pydantic import BaseModel


class Board(Base):
    title: str


class UpdateBoard(BaseModel):
    id: str
    title: str
