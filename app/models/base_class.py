from datetime import datetime
from pydantic import BaseModel, Field
from typing import Optional


class Base(BaseModel):
    created_date: Optional[datetime] = Field(default_factory=datetime.utcnow())


class ResponseModel(BaseModel):
    data: bytes = None
    status: int
    message: str
