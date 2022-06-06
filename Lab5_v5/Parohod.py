from Korabl import Korabl


class Parohod(Korabl):
    def __init__(self, water=600, skorost=500, istochnik_energy=3):
        super().__init__(water, skorost)
        self._istochnik_energy = istochnik_energy

    @property
    def istochnik_energy(self):
        return self._istochnik_energy

    @istochnik_energy.setter
    def istochnik_energy(self, istochnik_energy):
        self._istochnik_energy = istochnik_energy

    def edit(self):
        super().edit()
        self.istochnik_energy = input("Введите источник энергии: ")

    def __str__(self):
        return f"Водоизмещение: {self._water}, \n" \
               f"Скорость: {self._skorost}, \n" \
               f"Источник энергии: {self._istochnik_energy}"

