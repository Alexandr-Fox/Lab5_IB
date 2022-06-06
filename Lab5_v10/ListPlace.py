from Home import Home
from Locality import Locality
from Street import Street


class ListPlace:
    def __init__(self):
        self._list = list()

    @property
    def list(self):
        return self._list

    def addLocality(self):
        country = input("Введите название страны: ")
        town_name = input("Введите название населенного пункта: ")
        self._list.append(Locality(country, town_name))

    def addStreet(self):
        country = input("Введите название страны: ")
        town_name = input("Введите название населенного пункта: ")
        street_name = input("Введите название улицы: ")
        self._list.append(Street(street_name, town_name, country))

    def addHome(self):
        country = input("Введите название страны: ")
        town_name = input("Введите название населенного пункта: ")
        street_name = input("Введите название улицы: ")
        number = int(input("Введите номер дома: "))
        self._list.append(Home(number, street_name, town_name, country))

    def find(self):
        d = int(input(
            "Меню\n"
            "1) Населенный пункт\n"
            "2) Улицу\n"
            "3) Дом\n"
            "Выбирите что искать: "
        )
        )
        if d == 1:
            country = input("Введите название страны: ")
            town_name = input("Введите название населенного пункта: ")
            for i in self.list:
                if i.country == country and i.town_name == town_name:
                    print(i)
        if d == 2:
            country = input("Введите название страны: ")
            town_name = input("Введите название населенного пункта: ")
            street_name = input("Введите название улицы: ")
            for i in self.list:
                if isinstance(i, Street):
                    if i.country == country and i.town_name == town_name and i.street_name == street_name:
                        print(i)

        if d == 3:
            country = input("Введите название страны: ")
            town_name = input("Введите название населенного пункта: ")
            street_name = input("Введите название улицы: ")
            number = int(input("Введите номер дома: "))
            for i in self.list:
                if isinstance(i, Home):
                    if i.country == country and \
                            i.town_name == town_name and \
                            i.street_name == street_name and \
                            i.number == number:
                        print(i)

    def edit(self):
        d = int(input(
            "Меню\n"
            "1) Населенный пункт\n"
            "2) Улицу\n"
            "3) Дом\n"
            "Выбирите что изменить: "
        )
        )
        if d == 1:
            country = input("Введите название страны: ")
            town_name = input("Введите название населенного пункта: ")
            for i in self.list:
                if i.country == country and i.town_name == town_name:
                    i.edit()
        if d == 2:
            country = input("Введите название страны: ")
            town_name = input("Введите название населенного пункта: ")
            street_name = input("Введите название улицы: ")
            for i in self.list:
                if isinstance(i, Street):
                    if i.country == country and i.town_name == town_name and i.street_name == street_name:
                        i.edit()

        if d == 3:
            country = input("Введите название страны: ")
            town_name = input("Введите название населенного пункта: ")
            street_name = input("Введите название улицы: ")
            number = int(input("Введите номер дома: "))
            for i in self.list:
                if isinstance(i, Home):
                    if i.country == country and \
                            i.town_name == town_name and \
                            i.street_name == street_name and \
                            i.number == number:
                        i.edit()

    def delete(self):
        d = int(input(
            "Меню\n"
            "1) Населенный пункт\n"
            "2) Улицу\n"
            "3) Дом\n"
            "Выбирите что искать: "
        )
        )
        if d == 1:
            country = input("Введите название страны: ")
            town_name = input("Введите название населенного пункта: ")
            for i in self.list:
                if i.country == country and i.town_name == town_name:
                    print(i)
                    self._list.remove(i)
                    del i
        if d == 2:
            country = input("Введите название страны: ")
            town_name = input("Введите название населенного пункта: ")
            street_name = input("Введите название улицы: ")
            for i in self.list:
                if isinstance(i, Street):
                    if i.country == country and i.town_name == town_name and i.street_name == street_name:
                        print(i)
                        self._list.remove(i)
                        del i

        if d == 3:
            country = input("Введите название страны: ")
            town_name = input("Введите название населенного пункта: ")
            street_name = input("Введите название улицы: ")
            number = int(input("Введите номер дома: "))
            for i in self.list:
                if isinstance(i, Home):
                    if i.country == country and \
                            i.town_name == town_name and \
                            i.street_name == street_name and \
                            i.number == number:
                        print(i)
                        self._list.remove(i)
                        del i

    def __str__(self):
        res = ""
        for i in self.list:
            res += str(i)
            res += "\n"
        return res

    def __del__(self):
        del self._list
        print("Список удален")

    def print(self):
        print(self)

    @list.setter
    def list(self, value):
        self._list = value
