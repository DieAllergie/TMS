stroka = input('Введите строку: \n')
if len(stroka) % 2 == 0:
    i = int(len(stroka)/2 - 1)
    print(stroka[i])
    if stroka[0] == stroka[i]:
        print(stroka[1:-1])
else:
    i = int(len(stroka) / 2)
    print(stroka[i])
    if stroka[0] == stroka[i]:
        print(stroka[1:-1])

