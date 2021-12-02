class MyException(Exception):
    def __init__(self, message='У нас проблемы!!!'):
        super().__init__(message)
