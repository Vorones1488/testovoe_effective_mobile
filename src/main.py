import asyncio
from src.app_meny.basic_menu import App, SelectionEnum
from src.books.utils.generate_id import generete_id

app = App()


async def app_run():
    app_run = True
    while app_run:
        run_menu = SelectionEnum.start
        if run_menu == SelectionEnum.start:
            app.selection_menu(SelectionEnum.start)
        try:
            answer = int(input("ожидаение ввода: "))
            match answer:
                case 0:
                    generete_id.seve_lost_id()
                    app_run = False
                case 1:
                    await app.add_book()
                    generete_id.seve_lost_id()
                case 2:
                    try:
                        book = await app.put_book()
                        print("статус успешно обнолвен")
                    except TypeError as t:
                        print("книга не найдена")
                case 3:
                    status_del = await app.del_book_id()
                    if status_del:
                        print("книга успешно удалена")
                    else:
                        print("книга не найдена")
                case 4:
                    book_list = await app.get_all_books()
                    if book_list == []:
                        print("В вашей библиотеке книг не обнаружено")
                    else:
                        for book in book_list:
                            book = book.to_dict()
                            print("___________________________")
                            for key, value in book.items():
                                print(f"{key}: {value}")
                    input('для возврата в главное меню нажмити "enter"')
        except ValueError:
            print("введите числовое значение от 0 до 4")
        if 0 < answer > 3:
            print("введите число от 0 до 4")


# '1 - для добавление книги',
#             '2 - для редактирования книги',
#             '3 - для удаления книги',
#             '0 - для выхода из приложения'


asyncio.run(app_run())
