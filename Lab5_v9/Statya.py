from Rasdel import Rasdel


class Statya(Rasdel):
    def __init__(self, magazine_razdel="", magazine_statya="", magazine=""):
        super().__init__(magazine_razdel, magazine)
        self._magazine_statya = magazine_statya

    @property
    def magazine_statya(self):
        return self._magazine_statya

    @magazine_statya.setter
    def magazine_statya(self, magazine_statya):
        self._magazine_statya = magazine_statya

    def edit(self):
        self.magazine = input("Введите название журанала: ")
        self.magazine_razdel = input("Введите название раздела: ")
        self.magazine_statya = input("Введите название статьи: ")

    def __str__(self):
        return f"Журнал: {self.magazine}, " \
               f"Раздел: {self.magazine_razdel}, " \
               f"Статья: {self.magazine_statya} "
