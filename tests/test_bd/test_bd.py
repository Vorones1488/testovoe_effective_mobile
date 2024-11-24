import json
import os

from src.books.book_interface.interface_book import BookInterface
from src.books.book_model.book_mdb import Book
from src.books.repository.book_repo import JSONBookRepository
from src.books.utils.generate_id import GenerateID


class TestBD:
    path = "./db_test.json"

    def test_create_id(self):
        gen = GenerateID(id_path="./.test")
        id = gen.create_id()
        assert id == 1
        gen.seve_lost_id()
        id_lost = gen.create_id()
        assert id_lost == 2
        gen.seve_lost_id()
        with open("./.test", "r") as f:
            file_id = f.read()
            assert int(file_id) == id_lost
        os.remove("./.test")

    async def test_add_to_db(self):
        try:
            book = await JSONBookRepository.add(self, "test_title", "test_author", 1933)
            assert book.id == 1
            book2 = await JSONBookRepository.add(
                self, "test_title1", "test_author2", 1934
            )
            assert book2.id == 2
            book3 = await JSONBookRepository.add(
                self, "test_title1", "test_author2", 1934
            )
            assert book3.id == 3
        except AssertionError:
            os.remove(self.path)

        os.remove(self.path)

    async def test_get_book_to_id(self):

        count_book = 1
        while count_book <= 9:
            await JSONBookRepository.add(
                self,
                f"test_title{count_book}",
                f"test_author{count_book}",
                1930 + count_book,
            )
            count_book += 1

        book = await JSONBookRepository.get_key(self, "id", 5)
        try:
            assert isinstance(book, Book)
            assert book.id == 5
        except AssertionError:
            os.remove(self.path)

    async def test_get_all(self):
        book_list = await JSONBookRepository.get_all(self)
        assert isinstance(book_list, list)
        with open(self.path, "r", encoding="utf-8") as file:
            book_json = json.load(file)
            assert book_list[0].id == book_json[0]["id"]

    async def test_dell_id(self):
        result = await JSONBookRepository.dell_id(self, 5)
        assert result is True
        result = await JSONBookRepository.dell_id(self, 5)
        assert result is False

    async def test_put(self):
        status = "выдана"
        result = await JSONBookRepository.put(self, 6, status)
        with open(self.path, "r", encoding="utf-8") as file:
            book_json = json.load(file)
            for book in book_json:
                if book["id"] == 6:
                    assert book["status"] == status
        os.remove(self.path)
