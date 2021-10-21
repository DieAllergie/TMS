spisok = [1, 2, 3, 4, 5]
spisok2 = []
for i in range(1, len(spisok)):
    spisok2.append(spisok[i])
spisok2.append(spisok[0])
print(spisok2)

spisok3 = []
n = 1
while n < len(spisok):
    spisok3.append(spisok[n])
    n += 1
spisok3.append(spisok[0])
print(spisok3)

