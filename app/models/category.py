from .base_class import Base
from pydantic import BaseModel


class Category(Base):
    board_id: str
    title: str


class UpdateCategory(BaseModel):
    id: str
    title: str
