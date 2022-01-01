from typing import Dict, List
from .session import database
from .db_helpers import board_helper
from bson import ObjectId

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


async def edit_board(board: dict) -> Dict[str, str]:
    try:
        board_id = board["id"]
        ObjectId(board_id)  # check if id is valid

        board_found = await board_collection.find_one({"_id": ObjectId(board_id)})
        if board_found:
            await board_collection.update_one(
                {"_id": ObjectId(board_id)},
                {"$set": board},
            )
            updated_board = await board_collection.find_one(
                {"_id": ObjectId(board["id"])},
            )
            return board_helper(updated_board)
    except Exception:
        # TODO: return as an object, with status code
        raise TypeError("ID is invalid")


async def remove_board(board_id: str) -> Dict:
    board_object_id = set_object_id(board_id)
    removal_response = await board_collection.delete_one({"_id": board_object_id})
    if removal_response.deleted_count:
        response_obj = dict(status=200, message="Board has been deleted")
        return response_obj

    return False


# TODO: put this into a library file
def set_object_id(id_param: str) -> ObjectId:
    try:
        object_id = ObjectId(id_param)
        return object_id
    except Exception:
        raise TypeError("ID is not valid!")
