from fastapi import APIRouter, HTTPException
from app.models.base_class import ResponseModel
from app.models.category import Category, UpdateCategory
from app.database.category import insert_category, edit_category

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


@router.put(
    "/update", response_model=ResponseModel, response_description="Category Updated!"
)
async def update_category(category: UpdateCategory):
    response = await edit_category(category.dict())
    if response:
        return response
    raise HTTPException(404, "There is no category to update!")
