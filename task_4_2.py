tmp = [34, 4, 5, 65, 1, 12, 35, 77, 88]
amount1 = 0
amount2 = 0
for i in tmp:
    if i % 2 == 0:
        amount1 += 1

print(amount1)

n = 0
while n < len(tmp):
    if tmp[n] % 2 == 0:
        amount2 += 1
    n += 1
print(amount2)
