from typing import List
from fastapi import APIRouter
from app.database.boards import fetch_boards

router = APIRouter()


@router.get("/")
async def get_boards() -> List:
    boards = await fetch_boards()
    return boards


@router.post("/{title}")
def create_board(title: str):
    return "hello"
