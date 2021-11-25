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

    def __init__(self, h=0, m=0, s=0, time_str='', *args):
        if not args and not time_str and not h and not m and not s:
            self.hours = 0
            self.minutes = 0
            self.seconds = 0
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

    def __eq__(self, other: str):
        ls = list(other.split(':'))
        other_hours = int(ls[0])
        other_minutes = int(ls[1])
        other_seconds = int(ls[2])
        if self.hours == other_hours and self.minutes == other_minutes and self.seconds == other_seconds:
            print('Да времена одинаковые')
        else:
            print('Нет времена разные')

    def __ne__(self, other):
        ls = list(other.split(':'))
        other_hours = int(ls[0])
        other_minutes = int(ls[1])
        other_seconds = int(ls[2])
        if self.hours != other_hours or self.minutes != other_minutes or self.seconds != other_seconds:
            print('Да времена разные')
        else:
            print('Нет времена одинаковые')


a = MyTime(time_str='12:32:05')
b = MyTime(h=15, m=24, s=75)
c = MyTime(1, 0, 3)

print(a.hours, a.minutes, a.seconds)
print(b.hours, b.minutes, b.seconds)
print(c.hours, c.minutes, c.seconds)
print(c.show_time())
print(c.hours, c.minutes, c.seconds)
print(a.show_time())

a.__eq__('12:32:04')
a == '12:32:05'
a != '12:36:05'


'''elif self.hours > other_hours \
     or (self.hours == other_hours and self.minutes > other_minutes) \
     or (self.hours == other_hours and self.minutes == other_minutes and self.seconds > other_seconds):
print('Время больше')'''
