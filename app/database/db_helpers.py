def board_helper(board: dict) -> dict:
    return {
        "id": str(board["_id"]),
        "title": board["title"],
    }
