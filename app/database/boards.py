from typing import Dict, List, Union
from .session import database
from .db_helpers import board_helper, set_object_id

board_collection = database.boardstest


async def fetch_boards() -> List[Dict[str, str]]:
    boards_list = []
    boards_result = board_collection.find()

    async for board in boards_result:
        boards_list.append(board_helper(board))

    return boards_list


async def insert_board(board: dict) -> Dict[str, str]:
    insert_response = await board_collection.insert_one(board)
    new_board_dict = await board_collection.find_one(insert_response.inserted_id)
    return board_helper(new_board_dict)


async def edit_board(board: dict) -> Union[Dict, bool]:
    board_object_id = set_object_id(board["id"])
    edit_response = await board_collection.update_one(
        {"_id": board_object_id},
        {"$set": {"title": board["title"]}},
    )
    if edit_response.modified_count:
        modified_board = await board_collection.find_one({"_id": board_object_id})
        response_obj = dict(
            data=board_helper(modified_board),
            message="Board updated!",
            status=200,
        )
        return response_obj
    return False


async def remove_board(board_id: str) -> Union[Dict, bool]:
    board_object_id = set_object_id(board_id)
    removal_response = await board_collection.delete_one({"_id": board_object_id})
    if removal_response.deleted_count:
        response_obj = dict(status=200, message="Board has been deleted")
        return response_obj
    return False
