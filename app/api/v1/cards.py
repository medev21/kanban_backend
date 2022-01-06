from typing import Dict, List
from fastapi import APIRouter
from app.models.base_class import ErrorResponseModel, ResponseModel

router = APIRouter()


@router.post(
    "/create", response_model=ResponseModel, response_description="List created!"
)
def create_list() -> List:
    list_data = list.dict()
    return []
