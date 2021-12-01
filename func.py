from exceptions import MyException


def func_add(n: float, m: float) -> float:
    return n + m


def func_sub(n: float, m: float) -> float:
    return n - m


def func_mul(n: float, m: float) -> float:
    return n * m


def func_div(n: float, m: float) -> float:
    try:
        if m == 0:
            raise MyException('Делить на ноль нельзя!!!')
        else:
            return n / m
    except MyException as err:
        print(f'm = 0 - {err}')




