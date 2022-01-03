from datetime import datetime
from pydantic import BaseModel, Field
from typing import Dict, List, Optional, Union


class Base(BaseModel):
    created_date: Optional[datetime] = Field(default_factory=datetime.utcnow())


class ResponseModel(BaseModel):
    data: Union[Dict, List] = None
    status: int
    message: str
