def func_add(n: float, m: float) -> float:
    return n + m


def func_sub(n: float, m: float) -> float:
    return n - m


def func_mul(n: float, m: float) -> float:
    return n * m


def func_div(n: float, m: float) -> float:
    try:
        return n / m
    except ZeroDivisionError as err:
        print(f'm = 0 - {err}!!!')




