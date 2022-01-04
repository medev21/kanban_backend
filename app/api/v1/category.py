from fastapi import APIRouter

router = APIRouter()


@router.post("/{board_id}/{title}")
def create_list(title: str, board_id: int):
    return "hello"
