def lambda1(**kwargs):
    d = lambda **kwargs: {key*2: value for key, value in kwargs.items()}
    return d(**kwargs)

def main():
    print(lambda1(a=1, b=2, cc=3))


if __name__ == '__main__':
    main()

