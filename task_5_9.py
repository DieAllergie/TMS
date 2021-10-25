m = int(input("Введите нижнее значение диапазона:\n"))
n = int(input("Введите верхнее значение диапазона:\n"))

for i in range(m, n+1):
    sp = []
    for j in range(2, i // 2 + 1):
        if i % j == 0:
            sp.append(str(j))
    print('{}:{}'.format(i, ' '.join(sp)))

