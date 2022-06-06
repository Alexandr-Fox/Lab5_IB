class Korabl:
    def __init__(self, water=600, skorost=500):
        self._water = water
        self._skorost = skorost

    @property
    def water(self):
        return self._water

    @water.setter
    def water(self, water):
        self._water = water

    @property
    def skorost(self):
        return self._skorost

    @skorost.setter
    def skorost(self, skorost):
        self._skorost = skorost

    def print(self):
        print(self)

    def edit(self):
        self._water = int(input("Введите водоизмещение: "))
        self._skorost = int(input("Введите скорость: "))

    def __del__(self):
        print("Элемент удален")

    def __str__(self):
        return f"Водоизмещение: {self._water}, \n" \
               f"Скорость: {self._skorost}" \
