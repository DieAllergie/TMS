class Television:

    def __init__(self, model: str, diagonal: int, color: str):
        self.__model = model
        self.__diagonal = diagonal
        self.__color = color

    def t_on(self):
        print(f"{self.__model} TV ON")

    def t_off(self):
        print(f"{self.__model} TV OFF")

    def set_model(self, model: str):
        self.__model = model

    def get_model(self):
        return self.__model

    def set_diagonal(self, diagonal: str):
        self.__diagonal = diagonal

    def get_diagonal(self):
        return self.__diagonal

    def set_color(self, color: str):
        self.__color = color

    def get_color(self):
        return self.__color


tv1 = Television("samsung", 55, "black")
tv1.set_color("green")
print(tv1.get_color())
tv1.t_on()
