from enum import Enum

from src.books.utils.generate_id import generete_id


class StatusBook(Enum):
    true = "в налчии"
    false = "выдана"


class Book:
    def __init__(
        self,
        title: str = None,
        author: str = None,
        year: int = None,
        id=None,
        status: str = "в наличии",
    ):
        self.id = id
        self.title = title
        self.author = author
        self.year = year
        self.status = status

    def to_dict(self, to_bd: bool = False) -> dict:
        """Сreates a dictionary for input into the database"""
        if to_bd:
            self.id = generete_id.create_id()
            """создает словарь с полями модели"""
        book_dict = {
            "id": self.id,
            "title": self.title,
            "author": self.author,
            "year": self.year,
            "status": self.status,
        }
        return book_dict
