from Statya import Statya
from Locality import Locality
from Rasdel import Rasdel


class ListBook:
    def __init__(self):
        self._list = list()

    @property
    def list(self):
        return self._list

    def addLocality(self):
        magazine = input("Введите название журанала: ")
        self._list.append(Locality(magazine))

    def addRasdel(self):
        magazine = input("Введите название журанала: ")
        magazine_razdel = input("Введите название раздела: ")
        self._list.append(Rasdel(magazine_razdel, magazine))

    def addStatya(self):
        magazine = input("Введите название журанала: ")
        magazine_razdel = input("Введите название раздела: ")
        magazine_statya = input("Введите название статьи: ")
        self._list.append(Statya(magazine_statya, magazine_razdel, magazine))

    def find(self):
        print("Меню\n" "1) Журнал\n" "2) Раздел\n" "3) Статьи\n" "Выбирите что изменить: ")
        d = int(input())
        if d == 1:
            magazine = input("Введите название журанала: ")
            for i in self.list:
                if i.magazine == magazine:
                    print(i)
        if d == 2:
            magazine = input("Введите название журанала: ")
            magazine_razdel = input("Введите название раздела: ")
            for i in self.list:
                if isinstance(i, Rasdel):
                    if i.magazine == magazine and i.magazine_razdel == magazine_razdel:
                        print(i)

        if d == 3:
            magazine = input("Введите название журанала: ")
            magazine_razdel = input("Введите название раздела: ")
            magazine_statya = input("Введите название статьи: ")
            for i in self.list:
                if isinstance(i, Statya):
                    if i.magazine == magazine and \
                            i.magazine_statya == magazine_statya and \
                            i.magazine_razdel == magazine_razdel:
                        print(i)

    def edit(self):
        print("Меню\n" "1) Журнал\n" "2) Раздел\n" "3) Статьи\n" "Выбирите что изменить: ")
        d = int(input())
        if d == 1:
            magazine = input("Введите название журанала: ")
            for i in self.list:
                if i.magazine == magazine:
                    i.edit()
        if d == 2:
            magazine = input("Введите название журанала: ")
            magazine_razdel = input("Введите название раздела: ")
            for i in self.list:
                if isinstance(i, Rasdel):
                    if i.magazine == magazine and i.magazine_razdel == magazine_razdel:
                        i.edit()

        if d == 3:
            magazine = input("Введите название журанала: ")
            magazine_razdel = input("Введите название раздела: ")
            magazine_statya = input("Введите название статьи: ")
            for i in self.list:
                if isinstance(i, Statya):
                    if i.magazine == magazine and \
                            i.magazine_statya == magazine_statya and \
                            i.magazine_razdel == magazine_razdel:
                        i.edit()

    def delete(self):
        print("Меню\n" "1) Журнал\n" "2) Раздел\n" "3) Статьи\n" "Выбирите что изменить: ")
        d = int(input())
        if d == 1:
            magazine = input("Введите название журанала: ")
            town_name = input("Введите название населенного пункта: ")
            for i in self.list:
                if i.magazine == magazine and i.town_name == town_name:
                    print(i)
                    self._list.remove(i)
                    del i
        if d == 2:
            magazine = input("Введите название журанала: ")
            magazine_razdel = input("Введите название раздела: ")
            for i in self.list:
                if isinstance(i, Rasdel):
                    if i.magazine == magazine and i.magazine_razdel == magazine_razdel:
                        print(i)
                        self._list.remove(i)
                        del i

        if d == 3:
            magazine = input("Введите название журанала: ")
            magazine_razdel = input("Введите название раздела: ")
            magazine_statya = input("Введите название статьи: ")
            for i in self.list:
                if isinstance(i, Statya):
                    if i.magazine == magazine and \
                            i.magazine_statya == magazine_statya and \
                            i.magazine_razdel == magazine_razdel:
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
