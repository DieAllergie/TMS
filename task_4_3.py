dict1 = {'test': 'test_value', 'europe': 'eur', 'dollar': 'usd', 'ruble': 'rub'}
dict2 = {}
new_key = []
for key in dict1:
    key = key + str(len(key))
    new_key.append(key)
    print(key)
dict2 = dict(zip(new_key, list(dict1.values())))
print(dict2)

dict3 = {}
n = 0
new_key2 = []
while n < len(dict1.keys()):
    new_key2.append(list(dict1.keys())[n] + str(len(list(dict1.keys())[n])))
    n += 1
dict3 = dict(zip(new_key2, list(dict1.values())))
print(dict3)
