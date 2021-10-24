x = input("Введите число для обработки:\n")
summ = 0
pro = 1
for i in x:
    summ = summ + int(i)
    pro = pro * int(i)
print("сумма цифр числа {} равна {}, произведение цифр равно {}".format( x, summ, pro))