from classes import Math
from exceptions import MyException


def run_interface():
    operation = 'some'
    while operation != 0:
        print('1. Сложение')
        print('2. Вычитание')
        print('3. Умножение')
        print('4. Деление')
        print('0. Выход')

        flag = True
        while flag:
            operation = input('Выберете операцию: ')
            try:
                if str(operation).isdigit() and 0 <= int(operation) <= 4:
                    choice = int(operation)
                else:
                    raise MyException('Выберите коректный номер операции, которую хотите совершить!!!')
            except MyException as err:
                print(f'{err}')
                choice = None
                continue
            if choice:
                flag = False
        flag1 = True
        while flag1:
            try:
                n = int(input('Введите первое число: '))
            except ValueError:
                print(f'Введите число!!!')
                continue
            if n:
                flag1 = False
        flag2 = True
        while flag2:
            try:
                m = int(input('Введите второе чмсло: '))
            except ValueError:
                print(f'Введите число!!!!')
                continue
            if m:
                flag2 = False

        if choice == 0:
            break
        elif choice == 1:
            print('Результат сложения равен: ', Math(n, m).func_add())
        elif choice == 2:
            print('Результат вычитания равен: ', Math(n, m).func_sub())
        elif choice == 3:
            print('Результат умножения равен: ', Math(n, m).func_mul())
        elif choice == 4:
            print('Результат деления равен: ', Math(n, m).func_div())
