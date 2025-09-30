"""Book API"""
from fastapi import FastAPI
from pydantic import BaseModel
from uuid import UUID

app = FastAPI()

books = {}
books_data = {"id": 0, "title": "", "author": "", "publisher": "", "year": 0, "price": 0.0}


class Book(BaseModel):
    title: str
    author: str
    publisher: str
    year: int
    price: float



@app.get("/")
def root():
    return {
        "message": "Welcome to the Book API"
    }

@app.post("/add_book")
def add_book(book: Book):
    new_book = books_data.copy()
    new_book["id"] = str(UUID(int=len(books) + 1))
    new_book["title"] = book.title
    new_book["author"] = book.author
    new_book["publisher"] = book.publisher
    new_book["year"] = book.year
    new_book["price"] = book.price

    books[new_book["id"]] = new_book
    return new_book

@app.get("/books")
def get_books():
    return books

@app.get("/books/{id}")
def get_book(id: str):
    book = books.get(id)
    if not book:
        return {"error": "Book not found"}
    return book