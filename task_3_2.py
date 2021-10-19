guest = input('Введите количество гостей на свадьбе:\n')
if int(guest) > 50:
    print('Закажем ресторан.')
elif int(guest) <= 50 and int(guest) >= 20:
    print('Закажем кафе')
else:
    print('Останемся дома')

