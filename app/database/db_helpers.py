from bson import ObjectId


def response_helper(board: dict) -> dict:
    return {
        "id": str(board["_id"]),
        "title": board["title"],
    }


def set_object_id(id_param: str) -> ObjectId:
    try:
        object_id = ObjectId(id_param)
        return object_id
    except Exception:
        raise TypeError("ID is not valid!")
