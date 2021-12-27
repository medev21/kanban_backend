from .session import database

board_collection = database.boardstest


async def fetch_boards():
    # breakpoint()

    boards_list = []
    boards_result = board_collection.find()

    async for board in boards_result:
        obj = {
            "id": str(board["_id"]),
            "title": board["title"],
        }

        boards_list.append(obj)

    return boards_list
