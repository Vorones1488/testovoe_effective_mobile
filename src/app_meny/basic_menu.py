from enum import StrEnum, auto
from typing import Any

from src.books.book_interface.interface_book import BookInterface
from src.books.book_model.book_mdb import Book
from src.books.repository.book_repo import JSONBookRepository


class SelectionEnum(StrEnum):
    start = auto()


class Menu:
    def __init__(self, menu: list[str]):
        self.menu = menu

    def get_menu(self, action: str):
        """Displays menu list"""
        for name in self.menu:
            print(action, name)


class App:
    def __init__(
        self,
        star_menu: Menu = Menu(
            [
                "1 - для добавление книги",
                "2 - для редактирования книги",
                "3 - для удаления книги",
                "4 - для вывода списка всех имеющихся книг",
                "0 - для выхода из приложения",
            ]
        ),
        book_base: BookInterface = JSONBookRepository(),
    ):
        self.star_menu = star_menu
        self.book_base = book_base

    def selection_menu(
        self, selectet_meny: SelectionEnum, action: str = "введите"
    ) -> Any:
        """Displays the selected menu"""
        _MENUDICT = {
            SelectionEnum.start: self.star_menu.get_menu,
        }
        _MENUDICT[selectet_meny](action)

    async def add_book(self) -> Any:
        """Logic for adding a book to the database"""
        print("Меню добавления книги следуйте инструкции на экране")
        title = input("Введите название книги: ")
        author = input("Введете автора книги:")
        try:
            year = int(input("Ведите год издания: "))
            book = await self.book_base.add(title, author, year)
            print("успешно сохранен")
        except ValueError:
            y = True
            while y:
                try:
                    year = int(
                        input(
                            'Ведите год издания в числовом диапозоне больше 0 или "-1" для отмены : '
                        )
                    )
                    if year == -1:
                        print("отмена добавления")
                        break
                    else:
                        y = False
                        book = await self.book_base.add(title, author, year)
                        print("успешно сохранен")
                except ValueError:
                    y = True

    async def put_book(self) -> Any:
        """Book editing logic"""
        action_list = [
            "1 - для установки статуса на “в наличии”",
            "2 - для установки статуса на “выдана”",
            "0 - для выхода",
        ]
        print("Меню изменения статуса книги следуйте инструкции на экране")
        try:
            id = int(input("Введите id книги"))
        except ValueError:
            id = int(input("Введите id книги число больше 0"))
        for action in action_list:
            print(action)
        action = input("Введите действие: ")
        if action == "0":
            return "возврат в главное меню"
        elif action == "1":
            book = await self.book_base.put(id, "в наличии")
            return book
        elif action == "2":
            book = await self.book_base.put(id, "выдана")
            return book

    async def del_book_id(self) -> Any:
        """Deleting a book by id logic"""
        print("Меню изменения удаления книги следуйте инструкции на экране")
        id = int(input("Введите id книги"))
        status = await self.book_base.dell_id(id)
        return status

    async def get_all_books(self) -> list[Book]:
        "Logic for displaying all books"
        books = await self.book_base.get_all()
        return books
