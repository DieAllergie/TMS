fibonachi = [1, 1]
n = 15
for i in range(2, 15):
    fibonachi.append(fibonachi[i-2] + fibonachi[i-1])
print(fibonachi)

fibonachi1 = [1, 1]
m = 2
while m < 15:
    fibonachi1.append(fibonachi1[m-2] + fibonachi1[m-1])
    m += 1
print(fibonachi1)
