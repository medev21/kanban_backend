from .base_class import Base
from pydantic import BaseModel


class Category(Base):
    title: str


class UpdateCategory(BaseModel):
    id: str
    title: str
