from fastapi import FastAPI, Path, Query
from pydantic import BaseModel, Field
from starlette.responses import JSONResponse
from typing import Dict, Optional, List, Tuple
from starlette.types import Message
import uvicorn

app = FastAPI()


@app.get("/")
def index():
    return JSONResponse(content={"message": "Hello,  World"}, status_code=200)


@app.get("/profile/{name}")
def get_path_parameter(name: str):
    return JSONResponse(
        content={"message": f"My name is: {name}"},
        status_code=200,
    )


@app.get("/profile")
def get_query_parameter(start: int = 0, limit: int = 0):
    return JSONResponse(
        content={"message": f"start: {start} limit: {limit}"},
        status_code=200,
    )


@app.get("/books")
def get_books():
    books = [
        {
            "book_id": 1,
            "book_name": "Harry Potter and Philosopher's Stone",
            "page": 223,
        },
        {
            "book_id": 2,
            "book_name": "Harry Potter and the Chamber of Secrets",
            "page": 251,
        },
        {
            "book_id": 3,
            "book_name": "Harry Potter and the Prisoner of Azkaban",
            "page": 251,
        },
    ]
    return JSONResponse(content={"status": "ok", "data": books}, status_code=200)


@app.get("/books/{book_id}")
def get_books_by_id(book_id: int):
    dict_books = [
        {
            "book_id": 1,
            "book_name": "Harry Potter and Philosopher's Stone",
            "page": 223,
        },
        {
            "book_id": 2,
            "book_name": "Harry Potter and the Chamber of Secrets",
            "page": 251,
        },
        {
            "book_id": 3,
            "book_name": "Harry Potter and the Prisoner of Azkaban",
            "page": 251,
        },
    ]

    # หา book ที่ไอดีนั้นๆ
    book_filter = list(filter(lambda book: book["book_id"] == book_id, dict_books))

    # ตรวจสอบความถูกต้องของ result
    result = book_filter[0] if len(book_filter) > 0 else {}
    return JSONResponse(content={"status": "ok", "data": result}, status_code=200)


class createBooksPayload(BaseModel):
    id: str
    name: str
    page: int


@app.post("/books")
def create_books(req_body: createBooksPayload):
    req_body_dict = req_body.dict()

    id = req_body_dict["id"]
    name = req_body_dict["name"]
    page = req_body_dict["page"]

    print("[ Log ] name", id)
    print("[ Log ] name", name)
    print("[ Log ] page", page)

    mock_response = {
        "id": id,
        "name": name,
        "page": page,
    }
    return JSONResponse(
        content={"status": "ok", "data": mock_response}, status_code=201
    )


if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=3000, reload=True)