from datetime import datetime
from pydantic import BaseModel, Field
from typing import Dict, List, Optional, Union


class Base(BaseModel):
    created_date: Optional[datetime] = Field(default_factory=datetime.utcnow())


class ResponseBase(BaseModel):
    status: int
    message: str


class ResponseModel(ResponseBase):
    data: Union[Dict, List] = None


class ErrorResponseModel(ResponseBase):
    error: str
