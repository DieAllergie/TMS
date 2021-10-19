stroka = ''
while len(stroka) < 5:
    print('Введите строку длинной не менее 5 символов')
    stroka = input()
zd1 = stroka[2:3]
print('Третий символ строки:', zd1)
zd2 = stroka[-1]
print('Последний символ строки:', zd2)
zd3 = stroka[:5]
print('Первые пять символов строки:', zd3)
zd4 = stroka[:-2]
print('Строка без последних двух символов:', zd4)
zd5 = stroka[::2]
print('Символы строки с четными индексами', zd5)
