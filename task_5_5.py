import random
massiv = []
for i in range(0, 19):
    massiv.append(random.randint(0, 100))
print("Исходный массив", massiv)
max_number = max(massiv)
print("Максимально число массива равно:", max_number)
for i in range(len(massiv)):
    if massiv[i] % 2 == 0:
        massiv[i] = max_number
print("Измененный массив", massiv)

