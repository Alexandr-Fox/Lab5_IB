import sys
from ListPlace import ListPlace

# Ростовский Александр Евгеньевич вариант 10 повышеный уровень
if __name__ == "__main__":
    list_place = ListPlace()
    while True:
        try:
            d = int(input(f"Меню\n"
                          f"1) Добавить населенный пункт\n"
                          f"2) Добавить улицу\n"
                          f"3) Добавить дом\n"
                          f"4) Вывод на экран\n"
                          f"5) Изменить элемент\n"
                          f"6) Найти элемент\n"
                          f"7) Удалить элемент\n"
                          f"0) Выход\n"
                          f"Выбирите действие: "
                          ))
            if d == 1:
                list_place.addLocality()
            elif d == 2:
                list_place.addStreet()
            elif d == 3:
                list_place.addHome()
            elif d == 4:
                list_place.print()
            elif d == 5:
                list_place.edit()
            elif d == 6:
                list_place.find()
            elif d == 7:
                list_place.delete()
            elif d == 0:
                del list_place
                sys.exit(0)
            else:
                print("Неправильно выбрано действие")
        except ValueError:
            print("Неправильно выбрано действие")
