def my_decorator(func):
    def wrapper(ls: list) -> list:
        ls1 = []
        for i in range(len(ls)):
            if ls[i] % 2 != 0:
                ls1.append(ls[i])
        return ls1
    return wrapper

@my_decorator
def list_number(ls: list) -> list:
    l_n = ls
    return l_n


def main():
    ls = [1, 2, 3, 4, 5, 6, 7, 8]
    print(list_number(ls))


if __name__ == '__main__':
    main()

