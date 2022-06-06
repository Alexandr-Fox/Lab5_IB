from Locality import Locality


class Rasdel(Locality):
    def __init__(self, magazine_razdel = "", magazine = ""):
        super().__init__(magazine)
        self._magazine_razdel = magazine_razdel

    @property
    def magazine_razdel(self):
        return self._magazine_razdel

    @magazine_razdel.setter
    def magazine_razdel(self, magazine_razdel):
        self._magazine_razdel = magazine_razdel

    def edit(self):
        self.magazine = input("Введите название журанала: ")
        self.magazine_razdel = input("Введите название раздела: ")

    def __str__(self):
        return f"Журнал: {self.magazine}, " \
               f"Раздел: {self.magazine_razdel}"
