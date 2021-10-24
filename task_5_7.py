import random
import numpy
n = int(input("Введите размер матрицы:\n"))
matrix = numpy.random.randint(1, 100, size=(n, n))
print("Old matrix\n", matrix)
for i in range(n):
    matrix[i][i] = max(matrix[i])
print("New matrix", matrix)



