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


car1 = Car('Audi', 'A6', 2011, 100)
car1.speed_up()
car1.speed_now()
car1.speed_reversal()
car1.speed_now()
car1.speed_stop()
car1.speed_reversal()
