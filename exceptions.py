class MyException(Exception):
    def __init__(self, message='Ошибка!!! Что-то пошло не так!!!'):
        super().__init__(message)
