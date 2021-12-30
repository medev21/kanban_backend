from datetime import datetime
from pydantic import BaseModel, Field


class Base(BaseModel):
    created_date: datetime = Field(default_factory=datetime.utcnow())
