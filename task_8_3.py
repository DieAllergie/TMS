def sin1(x: float, eps: float) -> float:
    zn = x
    n = x
    i = 3
    while abs(n) > eps:
        n = n * (-1) * x * x / ((i - 1) * i)
        i += 2
        zn += n
    return zn


def main():
    eps = [0.00001, 0.01, 0.0001, 0.001, 0.1, 0.00000001]
    x = 3.14/2
    for item in eps:
        print(sin1(x, item))


if __name__ == '__main__':
    main()
