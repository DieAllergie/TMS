def fact2(n: int) -> int:
    itog = 1
    if n % 2 == 0:
        while n >= 2:
            itog = itog * n
            n = n - 2
    else:
        while n >= 1:
            itog = itog * n
            n = n - 2
    return itog


def main():
    ls = [5, 6, 7, 8, 9]
    print(list(fact2(i) for i in ls))


if __name__ == '__main__':
    main()

