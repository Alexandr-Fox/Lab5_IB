from Locality import Locality


class Street(Locality):
    def __init__(self, street_name="Республики", town_name="г. Тюмень", strana="Россия"):
        super().__init__(strana, town_name)
        self._street_name = street_name

    @property
    def street_name(self):
        return self._street_name

    @street_name.setter
    def street_name(self, street_name):
        self._street_name = street_name

    def edit(self):
        self.country = input("Введите название страны: ")
        self.town_name = input("Введите название населенного пункта: ")
        self.street_name = input("Введите название улицы: ")

    def __str__(self):
        return f"Улица {self.street_name}, " \
               f"Населенный пункт: {self.town_name}, " \
               f"Страна: {self.country}"
