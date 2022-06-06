import sys
from ListKorabl import ListKorabl

# Ростовский Александр Евгеньевич вариант 10 повышеный уровень
if __name__ == "__main__":
    list_animals = ListKorabl()
    while True:
        try:
            global list_animals
            d = int(input("Меню\n"
                          "1) Добавить корабль\n"
                          "2) Добавить парусник\n"
                          "3) Добавить пароход\n"
                          "4) Вывод на экран\n"
                          "5) Изменить элемент\n"
                          "6) Найти элемент\n"
                          "7) Удалить элемент\n"
                          "0) Выход\n"
                          "Выбирите действие: "
                          ))
            if d == 1:
                list_animals.addKorabl()
            elif d == 2:
                list_animals.addParusnik()
            elif d == 3:
                list_animals.addParohod()
            elif d == 4:
                list_animals.print()
            elif d == 5:
                list_animals.edit()
            elif d == 6:
                list_animals.find()
            elif d == 7:
                list_animals.delete()
            elif d == 0:
                del list_animals
                sys.exit(0)
            else:
                print("Неправильно выбрано действие")
        except ValueError:
            print("Неправильно выбрано действие")
