def sm_to_duim(a):
    print('{} см это {} дюйма'.format(a, round((a / 2.54), 2)))


def duim_to_sm(a):
    print('{} дюйма это {} см'.format(a, round((a * 2.54), 2)))


def mili_to_km(a):
    print(f'{a} мили это {round(a * 1.60934, 2)} км')


def km_to_mili(a):
    print(f'{a} км это {round(a / 1.60934, 2)} мили')


def fun_to_kg(a):
    print(f'{a} футнов это {round(a * 0.453592, 2)} кг')


def kg_to_fun(a):
    print(f'{a} кг это {round(a / 0.453592, 2)} фунта')


def unc_to_gr(a):
    print(f'{a} унций это {round(a * 28.3495, 2)} гр')


def gr_to_unc(a):
    print(f'{a} гр это {round(a / 28.3495, 2)} унции')


def gal_to_litr(a):
    print(f'{a} галлона это {round(a * 3.7854, 2)} литра')


def litr_to_gal(a):
    print(f'{a} литра это {round(a / 3.7854, 2)} галлона')


def pint_to_litr(a):
    print(f'{a} пинты это {round(a * 0.473177, 2)} литра')


def litr_to_pint(a):
    print(f'{a} литра это {round(a / 0.473177, 2)} пинты')


while True:
    print('Выберите операцию перевода единиц измерения\n'
          '1. Дюймы в сантиметры\n'
          '2. Сантиматры в дюймы\n'
          '3. Мили в киллометры\n'
          '4. Километры в мили\n'
          '5. Фунты в килограммы\n'
          '6. Килограммы в фунты\n'
          '7. Унции в граммы\n'
          '8. Граммы в унции\n'
          '9. Галлон в литры\n'
          '10. Литры в галлон\n'
          '11. Пинты в литры\n'
          '12. Литры в пинты\n'          
          '0. Выход')
    choice = int(input('Введите Ваш выбор: '))
    if choice == 0:
        break
    elif choice == 1:
        n = float(input('Введите количество сантиметров:'))
        sm_to_duim(n)
    elif choice == 2:
        n = float(input('Введите количество дюймов:'))
        duim_to_sm(n)
    elif choice == 3:
        n = float(input('Введите количество миль:'))
        mili_to_km(n)
    elif choice == 4:
        n = float(input('Введите количество км:'))
        km_to_mili(n)
    elif choice == 5:
        n = float(input('Введите количество фунтов:'))
        fun_to_kg(n)
    elif choice == 6:
        n = float(input('Введите количество кг:'))
        kg_to_fun(n)
    elif choice == 7:
        n = float(input('Введите количество унций:'))
        unc_to_gr(n)
    elif choice == 8:
        n = float(input('Введите количество грамм:'))
        gr_to_unc(n)
    elif choice == 9:
        n = float(input('Введите количество галлонов:'))
        gal_to_litr(n)
    elif choice == 10:
        n = float(input('Введите количество литров:'))
        litr_to_gal(n)
    elif choice == 11:
        n = float(input('Введите количество пинт:'))
        pint_to_litr(n)
    elif choice == 12:
        n = float(input('Введите количество литров:'))
        litr_to_pint(n)

