def sum_numbers(a : float, b : float):
    print("Сумма чисел равна", a+b)

def dif_numbers(a : float, b : float):
    print("Разность чисел равна", a-b)

def product_numbers(a : float, b : float):
    print("Произведение чисел равно", a*b)

def func_2(x : float, y : float):
    print("Вычисление формулы равно", (abs(x)-abs(y))/(1+abs(x*y)))

def cube(a : float):
    print("Объем куба равен", a**3)
    print("Площадь боковой грани равна", a**2)

def average_geometric(a : float, b : float):
    print("Среднее орифметическое равно", (a + b)/2)
    print("Среднее геометрическое равно -+", (a*b)**0.5)

def triangle(a : float, b : float):
    print("Гипотенуза треугольника равна", (a**2 + b**2)**0.5)
    print("Площадь треугольника равна", a*b*0.5)

sum_numbers(4, 5)
cube(3)
average_geometric(4, 4)