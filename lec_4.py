'''tmp = ""
summa = 0
while tmp != 'стоп':
    tmp = input('Введите число\n')
    if tmp != 'стоп' and tmp and int(tmp) % 5 != 0:
        summa += int(tmp)
print(summa)



spisok = [10, 5, 20, 40, 4, 50]
print(sum(spisok[i] for i in range(len(spisok)) if spisok[i] > 10))


import random
n = random.randint(0, 10)
while n != 7:
    print(n)
    n = random.randint(0, 10)
print("last number", n)




import random
from random import randint
n = int(input("Введите размер матрицы N\n"))
m = int(input("Введите размер матрицы M\n"))
matrix = [[random.randint(1, 9) for x in range(n)] for y in range(m)]

summa = 0
kol_vo = 0
for i in range(n):
    for j in range(m):
        if matrix[i][j] % 3 == 0:
            summa += matrix[i][j]
        if matrix[i][j] % 7 == 0:
            kol_vo +=1
print(matrix)
print("Сумма чисел равна", summa)
print(kol_vo, "встречается число 7")
'''
'''
summa = 0
for i in matrix:
    for j in i:
        summa += j

sr = summa / (n*m)
kol = 0
for i in range(n):
    for j in range(m):
        if matrix[i][j] > sr and (i + j) % 2 == 0:
            kol += 1

print(matrix)
print('Среднее арифметическое', sr)
print('Количество элементов', kol)
'''


'''
for i, elem in enumerate(['a','b','c','d']):
    print(f'{i} - {elem}')
'''
'''
pupils = [
{
'firstname': 'Masha',
'Group': 42,
'physics': 7,
'informatics': 6,
'history': 8,
},
{
'firstname': 'Masha1',
'Group': 42,
'physics': 7,
'informatics': 6,
'history': 8,
},
{
'firstname': 'Masha2',
'Group': 42,
'physics': 7,
'informatics': 6,
'history': 8,
},
]

for i in pupils:
    average = 0
    urok = 0
    for a, r in i.items():
        if a == "firrstname" or a == "group":
            continue
            arerage += r
            urok += 1
        x = average / urok
        if x >= 4:
            print(i)
'''
import random
n = int(input("Введите минимальное целое число\n"))
m = int(input("Введите максимальное целое число \n"))
k = int(input("Введите количество попыток \n"))

number = random.randint(n, m)
print(number)

f_number = int(input('Введите число от {} до {} у вас осталось {} попыток\n'.format(n, m, k)))


while f_number != number and k > 0:

    if f_number < number:
        n = f_number + 1
        k = k - 1
    else:
        m = f_number - 1
        k = k - 1

    if k == 0:
        print("попытки закончились")
        break
    f_number = int(input('Введите число от {} до {} у вас осталось {} попыток \n'.format(n, m, k)))



if number == f_number:
    print("You are winner")



