from fastapi import FastAPI
# from typing import Optional

app = FastAPI()


@app.get("/healthCheck")
def api_status():
    return "ok"


@app.post("/api/board/{title}")
def create_board(title: str):
    return 'hello'


@app.post("/api/list/{board_id}/{title}")
def create_list(title: str, board_id: int):
    return 'hello'


@app.post("/api/card/{list_id}/{title}")
def create_card(title: str, list_id: int):
    return 'hello world'

