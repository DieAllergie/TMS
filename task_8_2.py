def polindrom(word: str) -> bool:
    if word == word[::-1]:
        return True
    else:
        return False


def main():
    ls = ['last', 'lasal', 'neccen']
    for i in ls:
        if polindrom(i):
            print(f'слово {i} является полиндромом')
        else:
            print(f'слово {i} не является полиндромом')


if __name__ == '__main__':
    main()
