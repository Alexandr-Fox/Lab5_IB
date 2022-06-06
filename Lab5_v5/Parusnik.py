from Korabl import Korabl


class Parusnik(Korabl):
    def __init__(self, water=600, skorost=500, count_macht=3):
        super().__init__(water, skorost)
        self._count_macht = count_macht

    @property
    def count_macht(self):
        return self._count_macht

    @count_macht.setter
    def count_macht(self, count_macht):
        self._count_macht = count_macht

    def edit(self):
        super().edit()
        self.count_macht = int(input("Введите количество мачт: "))

    def __str__(self):
        return f"Водоизмещение: {self._water}, \n" \
               f"Скорость: {self._skorost}, \n" \
               f"Количество мачт: {self._count_macht}"
