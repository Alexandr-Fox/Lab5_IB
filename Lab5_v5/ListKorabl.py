from Parusnik import *
from Parohod import *


class ListKorabl:
    def __init__(self):
        self._list = list()

    @property
    def list(self):
        return self._list

    def addKorabl(self):
        a = Korabl()
        a.edit()
        self._list.append(a)

    def addParusnik(self):
        m = Parusnik()
        m.edit()
        self._list.append(m)

    def addParohod(self):
        a = Parohod()
        a.edit()
        self._list.append(a)

    def find(self):
        d = int(input(
            "Меню\n"
            "1) кораблль\n"
            "2) парусник\n"
            "3) пароход\n"
            "Выбирите что искать: "
        )
        )
        e = int(input("Введите водоизмещение: "))
        x = int(input("Введите скорость: "))
        if d == 1:
            for i in self.list:
                if i.water == e and i.skorost == x:
                    print(i)
        elif d == 2:
            l = int(input("Введите количество мачт: "))
            for i in self.list:
                if isinstance(i, Parusnik):
                    if i.water == e and i.skorost == x and i.count_macht == l:
                        print(i)

        elif d == 3:
            s = input("Введите источник энергии: ")
            for i in self.list:
                if isinstance(i, Parohod):
                    if i.water == e and i.skorost == x and i.istochnik_energy == s:
                        print(i)

    def edit(self):
        d = int(input(
            "Меню\n"
            "1) кораблль\n"
            "2) парусник\n"
            "3) пароход\n"
            "Выбирите что искать: "
        )
        )
        e = int(input("Введите водоизмещение: "))
        x = int(input("Введите скорость: "))
        if d == 1:
            for i in self.list:
                if i.water == e and i.skorost == x:
                    i.edit()
        elif d == 2:
            l = int(input("Введите количество мачт: "))
            for i in self.list:
                if isinstance(i, Parusnik):
                    if i.water == e and i.skorost == x and i.count_macht == l:
                        i.edit()

        elif d == 3:
            s = input("Введите источник энергии: ")
            for i in self.list:
                if isinstance(i, Parohod):
                    if i.water == e and i.skorost == x and i.istochnik_energy == s:
                        i.edit()

    def delete(self):
        d = int(input(
            "Меню\n"
            "1) кораблль\n"
            "2) парусник\n"
            "3) пароход\n"
            "Выбирите что искать: "
        )
        )
        e = int(input("Введите водоизмещение: "))
        x = int(input("Введите скорость: "))
        if d == 1:
            for i in self.list:
                if i.water == e and i.skorost == x:
                    del i
        elif d == 2:
            l = int(input("Введите количество мачт: "))
            for i in self.list:
                if isinstance(i, Parusnik):
                    if i.water == e and i.skorost == x and i.count_macht == l:
                        del i

        elif d == 3:
            s = input("Введите источник энергии: ")
            for i in self.list:
                if isinstance(i, Parohod):
                    if i.water == e and i.skorost == x and i.istochnik_energy == s:
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
