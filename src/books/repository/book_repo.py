import json
import os
from enum import EnumType
from typing import List

from src.books.book_interface.interface_book import BookInterface
from src.books.book_model.book_mdb import Book
from src.books.utils.algoritms import binary_search
from src.core.interface_core.model import AbstractModel


class JSONBookRepository(BookInterface):
    path = "./database/books.json"

    async def add(self, title: str, author: str, year: int) -> Book | dict:
        """Adding a book to the database"""
        try:
            isinstance(title, str)
        except TypeError as t:
            return {"error": 'неверный формат "title" введите строковое значение'}
        try:
            isinstance(author, str)
        except TypeError as t:
            return {"error": 'неверный формат "author" введите строковое значение'}
        try:
            isinstance(year, int)
            if year <= 0:
                return {
                    "error": 'неверный формат "year" введите числовое значение больше нуля'
                }
        except TypeError:
            return {
                "error": 'неверный формат "year" введите числовое значение больше нуля'
            }
        book = Book(title=title, author=author, year=year)
        if not os.path.exists(self.path):
            # Запись в файл только если он не существует.
            with open(self.path, "x", encoding="utf-8") as f:
                json.dump([book.to_dict(to_bd=True)], f, indent=4, ensure_ascii=False)

        else:
            with open(self.path, "r", encoding="utf-8") as file:
                book_json = json.load(file)
            book_json.append(book.to_dict(to_bd=True))

            with open(self.path, "w", encoding="utf-8") as file:
                json.dump(book_json, file, indent=4, ensure_ascii=False)
        return book

    async def get_key(self, search_object: str, value: str | int) -> Book | None:
        """Getting a book by field"""
        with open(self.path, "r", encoding="utf-8") as file:
            book_json = json.load(file)
            try:
                book = await binary_search(book_json, value, key=search_object)
            except ValueError:
                return None
            return Book(**book)

    async def get_all(self) -> List[Book]:
        """Returns a list of books"""

        with open(self.path, "r", encoding="utf-8") as file:
            book_json = json.load(file)
            books = [Book(**book) for book in book_json]
        return books

    async def dell_id(self, id: int) -> bool:
        """Deletes a book ee id"""
        with open(self.path, "r", encoding="utf-8") as file:
            book_json = json.load(file)
            book = await binary_search(book_json, id)
            try:
                book_json.remove(book)
                with open(self.path, "w", encoding="utf-8") as file:
                    json.dump(book_json, file, indent=4, ensure_ascii=False)
                return True
            except ValueError:
                return False

    async def put(self, id: int, status: str) -> bool:
        """Edits the status of a book by its id"""
        try:
            with open(self.path, "r", encoding="utf-8") as file:
                book_json = json.load(file)
                book = await binary_search(book_json, id)
                book["status"] = status
                with open(self.path, "w", encoding="utf-8") as file:
                    json.dump(book_json, file, indent=4, ensure_ascii=False)
                return book
        except FileNotFoundError:
            raise {"error": "файл не найден"}
        except TypeError:
            raise {"error": "неверный тип"}
