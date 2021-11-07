def my_decorator(func):
    def wrapper(*args):
        args = args[::-1]
        return args
    return wrapper


@my_decorator
def f(*args):
    pass


def main():
    print(f(1, 3, '344'))


if __name__ == '__main__':
    main()

