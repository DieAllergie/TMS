ln = input("Введите строку для обработки:\n")
sp = ln.split(' ')
sp = list(reversed(sp))
new_ln = ' '.join(sp)
print(new_ln)

