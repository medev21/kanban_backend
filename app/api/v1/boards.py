from fastapi import APIRouter

router = APIRouter()


@router.post("/{title}")
def create_board(title: str):
    return "hello"
