from typing import List
from .session import database
from .db_helpers import board_helper

board_collection = database.boardstest


async def fetch_boards() -> List:
    boards_list = []
    boards_result = board_collection.find()

    async for board in boards_result:
        boards_list.append(board_helper(board))

    return boards_list
