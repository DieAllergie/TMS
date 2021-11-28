class MyTime:
    def check_time(self):
        while self.seconds > 60:
            self.seconds -= 60
            self.minutes += 1
        while self.minutes > 60:
            self.minutes -= 60
            self.hours += 1
        while self.hours > 24:
            self.hours -= 24

        while self.seconds < 0:
            self.seconds += 60
            self.minutes -= 1
        while self.minutes < 0:
            self.minutes += 60
            self.hours -= 1
        while self.hours < 0:
            self.hours += 24

    def __init__(self, h=None, m=None, s=None, time_str=None, my_time=None):
        if not my_time and not time_str and not h and not m and not s:
            self.hours = 0
            self.minutes = 0
            self.seconds = 0
        elif type(my_time) == MyTime:
            self.hours = my_time.hours
            self.minutes = my_time.minutes
            self.seconds = my_time.seconds
        elif time_str:
            ls = list(time_str.split(':'))
            self.hours = int(ls[0])
            self.minutes = int(ls[1])
            self.seconds = int(ls[2])
        elif h or m or s:
            self.hours = h
            self.minutes = m
            self.seconds = s
        self.check_time()

    def show_time(self):
        show_time_str = ''
        if self.hours < 10:
            show_time_str += f'0{self.hours}'
        else:
            show_time_str += f'{self.hours}'

        if self.minutes < 10:
            show_time_str += f':0{self.minutes}'
        else:
            show_time_str += f':{self.minutes}'

        if self.seconds < 10:
            show_time_str += f':0{self.seconds}'
        else:
            show_time_str += f':{self.seconds}'

        return show_time_str

    def __eq__(self, my_time) -> bool:
        if self.hours == my_time.hours and self.minutes == my_time.minutes and self.seconds == my_time.seconds:
            print('Да времена одинаковые')
            return True
        else:
            print('Нет времена разные')
            return False

    def __ne__(self, my_time) -> bool:
        if self.hours != my_time.hours or self.minutes != my_time.minutes or self.seconds != my_time.seconds:
            print('Да времена разные')
            return True
        else:
            print('Нет времена одинаковые')
            return False

    def __ge__(self, my_time) -> bool:
        if self.hours > my_time.hours or (self.hours == my_time.hours and self.minutes > my_time.minutes)\
                or (self.hours == my_time.hours and self.minutes == my_time.minutes
                    and self.seconds >= my_time.seconds):
            print('Да время больше или равно')
            return True
        else:
            print('Нет время не бильше или равно')
            return False

    def __le__(self, my_time) -> bool:
        if self.hours < my_time.hours or (self.hours == my_time.hours and self.minutes < my_time.minutes)\
                or (self.hours == my_time.hours and self.minutes == my_time.minutes
                    and self.seconds <= my_time.seconds):
            print('Да время меньше или равно')
            return True
        else:
            print('Нет время не меньше или равно')
            return False

    def __lt__(self, my_time):
        if self.hours < my_time.hours or (self.hours == my_time.hours and self.minutes < my_time.minutes)\
                or (self.hours == my_time.hours and self.minutes == my_time.minutes
                    and self.seconds < my_time.seconds):
            print('Да время меньше')
            return True
        else:
            print('Нет время не меньше')
            return False

    def __gt__(self, my_time) -> bool:
        if self.hours > my_time.hours or (self.hours == my_time.hours and self.minutes > my_time.minutes)\
                or (self.hours == my_time.hours and self.minutes == my_time.minutes
                    and self.seconds > my_time.seconds):
            print('Да время больше')
            return True
        else:
            print('Нет время не бильше')
            return False

    def __add__(self, my_time):
        self.hours += my_time.hours
        self.minutes += my_time.minutes
        self.seconds += my_time.seconds
        self.check_time()
        return self

    def __mul__(self, n: int = 1):
        self.hours *= n
        self.minutes *= n
        self.seconds *= n
        self.check_time()
        return self

    def __sub__(self, my_time):
        self.hours -= my_time.hours
        self.minutes -= my_time.minutes
        self.seconds -= my_time.seconds
        self.check_time()
        return self


a = MyTime(time_str='12:32:05')
b = MyTime(h=12, m=32, s=6)
c = MyTime(1, 0, 3)
d = MyTime(my_time=a)
print(a.hours, a.minutes, a.seconds)
print(b.hours, b.minutes, b.seconds)
print(c.hours, c.minutes, c.seconds)
print(c.show_time())
print(c.hours, c.minutes, c.seconds)
print(a.show_time())
print(d.hours)

print(a == c)
print(a != d)
print(a >= b)
print(a <= b)
print(a < b)
print(a > b)
print((a + b).show_time())
print((a*2).show_time())
print((a-b).show_time())

