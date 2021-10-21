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
'''

