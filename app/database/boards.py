from typing import Dict, List
from .session import database
from .db_helpers import board_helper

board_collection = database.boardstest


async def fetch_boards() -> List[Dict[str, str]]:
    boards_list = []
    boards_result = board_collection.find()

    async for board in boards_result:
        boards_list.append(board_helper(board))

    return boards_list


async def add_board(board: dict) -> Dict[str, str]:
    insert_response = await board_collection.insert_one(board)
    new_board_dict = await board_collection.find_one(insert_response.inserted_id)
    return board_helper(new_board_dict)
