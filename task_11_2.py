class Car:
    def __init__(self, brand: str, model: str, year_prod: int, speed: int = 0):
        self.__brand = brand
        self.__model = model
        self.__year_prod = year_prod
        self.__speed = speed
        print(f'Init new {self.__brand} {self.__model} car complete')

    def set_brand(self, brand: str):
        self.__brand = brand

    def get_brand(self):
        return self.__brand

    def set_model(self, model: str):
        self.__model = model

    def get_model(self):
        return self.__model

    def set_year_prod(self, year_prod: int):
        self.__year_prod = year_prod

    def get_year_prod(self):
        return self.__year_prod

    def set_speed(self, speed: int):
        self.__speed = speed

    def get_speed(self):
        return self.__speed

    def speed_up(self):
        self.__speed += 5
        print('Speed up on 5 km/h')
        return self.__speed

    def speed_down(self):
        self.__speed -= 5
        print('Speed down on 5 km/h')
        return self.__speed

    def speed_stop(self):
        self.__speed = 0
        print('Car STOP. Speed equals 0 km/h')
        return self.__speed

    def speed_now(self):
        return print(f'Speed {self.__brand} {self.__model} равна {self.__speed} km/h')

    def speed_reversal(self):
        if self.__speed == 0:
            print('The car don\'t turn around because speed 0 km/h. Change please speed.')
        else:
            self.__speed *= (-1)
            print('The car turn around')
            return self.__speed


class SportCar(Car):
    def __init__(self, brand: str, model: str, year_prod: int, speed: int = 0):
        super().__init__(brand, model, year_prod, speed)

    def speed_up(self):
        self._Car__speed += 10
        print('Speed up on 10 km/h')
        return self._Car__speed

    def speed_down(self):
        self._Car__speed -= 10
        print('Speed down on 10 km/h')
        return self._Car__speed


class Truck(Car):
    def __init__(self, brand: str, model: str, year_prod: int, speed: int = 0):
        super().__init__(brand, model, year_prod)
        if speed > 40:
            print('The truck cannot go faster 40 km/h. Speed is set 40 km/h.')
            self._Car__speed = 40
        elif speed < -40:
            print('The truck cannot go faster -40 km/h. Speed is set -40 km/h.')
            self._Car__speed = -40
        else:
            self._Car__speed = speed

    def speed_up(self):

        if self._Car__speed + 5 > 40:
            print('The truck cannot go faster 40 km/h. Speed is set 40 km/h.')
            self._Car__speed = 40
        else:
            self._Car__speed += 5

    def speed_down(self):
        if self._Car__speed - 5 < -40:
            print('The truck cannot go faster -40 km/h. Speed is set -40 km/h.')
            self._Car__speed = -40
        else:
            self._Car__speed -= 5


class ElectroCar(Car):
    def __init__(self, brand: str, model: str, year_prod: int, speed: int = 0, energy: int = 100):
        super().__init__(brand, model, year_prod)
        if energy > 100:
            print('Battery charge can not be more 100%. Battery charge is set 100%.')
            self.__energy = 100
        elif energy < 0:
            print('Battery charge not be less 0%. Battery charge is set 0%.')
            self.__energy = 0
        else:
            self.__energy = energy
        if self.__energy < 50 and speed > 40:
            print('Low battery charge. Speed can not be more 40 km/h. Speed is set 40 km/h.')
            self._Car__speed = 40
        elif self.__energy < 50 and speed < -40:
            print('Low battery charge. Speed can not be less -40 km/h. Speed is set -40 km/h.')
            self._Car__speed = -40
        else:
            self._Car__speed = speed

    def speed_up(self):
        if self.__energy < 50:
            print('Low battery charge. Speed can not be more 40 km/h. Speed is set 40 km/h.')
            self._Car__speed = 40
        else:
            self._Car__speed += 5

    def speed_down(self):
        if self.__energy < 50:
            print('Low battery charge. Speed can not be less -40 km/h. Speed is set -40 km/h.')
            self._Car__speed = -40
        else:
            self._Car__speed -= 5

    def get_level_charge(self):
        print(f'Battery charge is {self.__energy}%.')
        return self.__energy

    def set_level_charge(self, energy: int = 100):
        if energy > 100:
            print('Battery charge can not be more 100%. Battery charge is set 100%.')
            self.__energy = 100
        elif energy < 0:
            print('Battery charge can not be less 0%. Battery charge is set 0%.')
            self.__energy = 0
        else:
            self.__energy = energy
        print(f'Battery charge is set {self.__energy}%.')


car1 = Car('Audi', 'A6', 2011, 100)
car1.speed_up()
car1.speed_now()
car1.speed_reversal()
car1.speed_now()
car1.speed_stop()
car1.speed_reversal()

car2 = SportCar('Ferrari', '488 Pista', 2019, 150)
car2.speed_up()
car2.speed_down()
car2.speed_down()
car2.speed_now()

car3 = Truck('Volvo', 'Euro 5', 2020, 36)
car3.speed_now()
car3.speed_up()
car3.speed_now()

car4 = ElectroCar('Tesla', 'Model S', 2021, 100, 40)
car4.speed_now()
car4.speed_up()
car4.speed_now()
car4.get_level_charge()
car4.set_level_charge(99)

