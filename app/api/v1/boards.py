from typing import Dict, List
from fastapi import APIRouter, HTTPException
from app.database.boards import add_board, fetch_boards
from app.models.board import Board

router = APIRouter()


@router.get("/", response_description="List of boards!")
async def get_boards() -> List:
    boards = await fetch_boards()
    return boards


@router.post("/create", response_description="Board Created!")
async def create_board(board: Board) -> Dict:
    board_data = board.dict()
    response = await add_board(board_data)
    if response:
        return response
    raise HTTPException(400, "Something went wrong creating the board")
