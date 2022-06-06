class Locality:
    def __init__(self, magazine="Men's helth"):
        self._magazine = magazine

    @property
    def magazine(self):
        return self._magazine

    @magazine.setter
    def magazine(self, magazine):
        self._magazine = magazine

    def print(self):
        print(self)

    def edit(self):
        self.magazine = input("Введите название журнала: ")

    def __del__(self):
        print("Элемент удален")

    def __str__(self):
        return f"Журнал: {self._magazine}"
