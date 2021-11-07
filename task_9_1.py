def format_str(ls: list) -> list:
    d = [{i + 1: ls[i]} for i in range(len(ls))]
    return d


def main():
    ls = ['asd', 'qwerty', 'tyty', 'a', 'qazwsx']
    x = format_str(ls)
    print(x)


if __name__ == '__main__':
    main()

