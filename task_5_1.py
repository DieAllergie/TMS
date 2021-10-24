list_operation = ['*', '-', '+', '/', '0']
sing = ''
while True:
    while sing not in list_operation:
        sing = input("Введите операцию (*, /, -, + или 0 - выход)\n")
    if sing == '0':
        break
    x = int(input("Введите первый операнд Х:\n"))
    y = int(input("Введите второй операнд Y:\n"))
    while sing == '/' and y == 0:
        print('Делить на 0 нельзя \n')
        y = int(input("Введите второй операнд Y:\n"))
    if sing == '/':
        z = x / y
    elif sing == '*':
        z = x * y
    elif sing == '-':
        z = x - y
    elif sing == '+':
        z = x + y
    print('{} {} {} равно {}'.format(x, sing, y, z))
    sing = ''
