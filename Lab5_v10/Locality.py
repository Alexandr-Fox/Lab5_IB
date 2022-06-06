class Locality:
    def __init__(self, strana="Россия", town_name="г. Тюмень"):
        self._country = strana
        self._town_name = town_name

    @property
    def country(self):
        return self._country

    @country.setter
    def country(self, country):
        self._country = country

    @property
    def town_name(self):
        return self._town_name

    @town_name.setter
    def town_name(self, town_name):
        self._town_name = town_name

    def print(self):
        print(self)

    def edit(self):
        self.country = input("Введите название страны: ")
        self.town_name = input("Введите название населенного пункта: ")

    def __del__(self):
        print("Элемент удален")

    def __str__(self):
        return f"Название: {self._town_name}, " \
               f"Страна: {self._country}"
