class MyException(Exception):
    def __init__(self, message='У нас проблемы!!!'):
        super().__init__(message)


class Book:
    def __init__(self, pages: int, year: int, author: str, price: int):
        try:
            if str(pages).isdigit() and int(pages) >= 0:
                self.pages = int(pages)
            else:
                raise MyException('Введите кол-во страниц!!! Целое число больше ноля!!!')
        except MyException as err:
            print(f'{err}')
        self.year = year
        self.author = author
        try:
            if str(price).isdigit() and int(price) > 0:
                self.price = int(price)
            else:
                raise MyException('Цена не может быть отрицательной!!!')
        except MyException as err:
            print(f'{err}')


book = Book(50.4, 2012, 'Family', -50)
#print(book.pages)
