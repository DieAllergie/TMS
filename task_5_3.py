n = 200
m = 300
list_del = []
for i in range(n, m + 1):
    summ = sum(j for j in range(1, i // 2 + 1) if i % j == 0)
    list_del.append(summ)
    #print('чмсло {} имеет сумму делителей {}'.format(i, summ))
#print(list_dict)
for i in range(len(list_del)):
    for j in range(i + 1, len(list_del)):
        #print(list_dict[i].values(), list_dict[j].values())
        if int(list_del[i]) == int(list_del[j]):
            print('Числа {} и {} являются являются дружественными\n'.format(i + n, j + n))
