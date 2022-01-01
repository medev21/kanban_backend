from bson import ObjectId


def board_helper(board: dict) -> dict:
    return {
        "id": str(board["_id"]),
        "title": board["title"],
    }


# TODO: ADD TYPING IN THIS FUNCTION
async def find_by_object_id(collection, id_param):
    response = collection.find_one({"_id": ObjectId(id_param)})
    return response


def set_object_id(id_param: str) -> ObjectId:
    try:
        object_id = ObjectId(id_param)
        return object_id
    except Exception:
        raise TypeError("ID is not valid!")
