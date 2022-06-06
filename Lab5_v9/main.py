import sys
from ListBook import ListBook


if __name__ == "__main__":
    list_book = ListBook()
    while True:
        try:
            d = int(input(f"Меню\n"
                          f"1) Добавить журнал\n"
                          f"2) Добавить раздел\n"
                          f"3) Добавить статью\n"
                          f"4) Вывод на экран\n"
                          f"5) Изменить элемент\n"
                          f"6) Найти элемент\n"
                          f"7) Удалить элемент\n"
                          f"0) Выход\n"
                          f"Выбирите действие: "
                          ))
            if d == 1:
                print("")
                list_book.addLocality()
                print("")
            elif d == 2:
                print("")
                list_book.addRasdel()
                print("")
            elif d == 3:
                print("")
                list_book.addStatya()
                print("")
            elif d == 4:
                print("")
                list_book.print()
                print("")
            elif d == 5:
                print("")
                list_book.edit()
                print("")
            elif d == 6:
                print("")
                list_book.find()
                print("")
            elif d == 7:
                print("")
                list_book.delete()
                print("")
            elif d == 0:
                del list_book
                sys.exit(0)
            else:
                print("Неправильно выбрано действие")
        except ValueError:
            print("Неправильно выбрано действие")
