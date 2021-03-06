from fastapi import APIRouter
from app.api.v1 import boards, cards, category

api_router = APIRouter()
api_router.include_router(boards.router, prefix="/boards", tags=["Boards"])
api_router.include_router(cards.router, prefix="/cards", tags=["Cards"])
api_router.include_router(category.router, prefix="/lists", tags=["Lists"])
