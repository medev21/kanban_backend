from fastapi import APIRouter

router = APIRouter()


@router.post("/{list_id}/{title}")
def create_list(title: str, list_id: int):
    return "hello"
