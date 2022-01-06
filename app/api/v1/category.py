from fastapi import APIRouter, HTTPException
from app.models.base_class import ErrorResponseModel, ResponseModel
from app.models.category import Category
from app.database.category import insert_category

router = APIRouter()


@router.post(
    "/create",
    response_model=ResponseModel,
    response_description="Category created!",
)
async def create_category(category: Category):
    response = await insert_category(category.dict())
    if response:
        return response
    raise HTTPException(500, "Something went wrong!")
