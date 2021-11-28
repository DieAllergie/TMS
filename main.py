import func


def main():
    operation = 'some'
    while operation != 0:
        print('1. Сложение')
        print('2. Вычитание')
        print('3. Умножение')
        print('4. Деление')
        print('0. Выход')
        operation = int(input('Выберете операцию: '))
        if operation == 0:
            break
        if operation in (0, 1, 2, 3, 4):
            try:
                n = int(input('Введите первое число: '))
            except ValueError as err:
                print(f'Введите допусимое значение {err}!!!!')
                continue
            try:
                m = int(input('Введите второе чмсло: '))
            except ValueError as err:
                print(f'Введите допусимое значение {err}!!!!')
                continue
            if operation == 1:
                print('Результат сложения равен: ', func.func_add(n, m))
            elif operation == 2:
                print('Результат вычитания равен: ', func.func_sub(n, m))
            elif operation == 3:
                print('Результат умножения равен: ', func.func_mul(n, m))
            elif operation == 4:
                print('Результат деления равен: ', func.func_div(n, m))
        else:
            print('Не правильная операция. Повторите выбор.')


if __name__ == '__main__':
    main()

