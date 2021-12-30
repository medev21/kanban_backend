from typing import Dict, List
from fastapi import APIRouter, HTTPException
from app.database.boards import insert_board, edit_board, fetch_boards
from app.models.board import Board, UpdateBoard

router = APIRouter()


@router.get("/", response_description="List of boards!")
async def get_boards() -> List:
    boards = await fetch_boards()
    return boards


@router.post("/create", response_description="Board Created!")
async def create_board(board: Board) -> Dict:
    board_data = board.dict()
    response = await insert_board(board_data)
    if response:
        return response
    raise HTTPException(400, "Something went wrong creating the board")


@router.put("/update", response_description="Board Update!")
async def update_board(board: UpdateBoard) -> Dict:
    response = await edit_board(board.dict())
    if response:
        return response
    raise HTTPException(404, "There is no board to update")


"""
@router.delete("/delete", response_description="Board Deleted!")
async def delete_board(id: int) -> Dict:
    return True
"""
