from Street import Street


class Home(Street):
    def __init__(self, number=1, street_name="Республики", town_name="г. Тюмень", strana="Россия"):
        super().__init__(street_name, town_name, strana)
        self._number = number

    @property
    def number(self):
        return self._number

    @number.setter
    def number(self, number):
        if number > 0:
            self._number = number

    def edit(self):
        self.country = input("Введите название страны: ")
        self.town_name = input("Введите название населенного пункта: ")
        self.street_name = input("Введите название улицы: ")
        self.number = int(input("Введите номер дома: "))

    def __str__(self):
        return f"Дом: {self.number}, " \
               f"Улица: {self.street_name}, " \
               f"Населенный пункт: {self.town_name}, " \
               f"Страна: {self.country}"
