class Math:
    def __init__(self, n: float, m: float):
        self.n = n
        self.m = m

    def func_add(self) -> float:
        return self.n + self.m

    def func_sub(self) -> float:
        return self.n - self.m

    def func_mul(self) -> float:
        return self.n * self.m

    def func_div(self) -> float:
        try:
            return self.n / self.m
        except ZeroDivisionError as err:
            print(f'm не может быть равно 0 - {err}!!!')

