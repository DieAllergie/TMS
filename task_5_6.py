import random

massiv = []
kol_cep = 0
n = int(input("Введите количество элементов в массиве:\n"))
for i in range(n):
    massiv.append(random.randint(0, 100))
print("Исходный массив", massiv)

i = 0
while i < n - 1:
    dl = 1
    j = i
    while j < n - 1 and massiv[j] < massiv[j + 1]:
        dl = dl + 1
        j = j + 1
    if dl > 1:
        kol_cep += 1
    i = i + dl

print("количество срезов: ", kol_cep)

