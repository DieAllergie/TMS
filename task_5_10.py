import datetime
dictionary = [{'train_number': 1001, 'st_out': 'Minsk', 't_out': '10:30:00', 'st_in': 'Moscow', 't_in': '19:45:00'},
              {'train_number': 1002, 'st_out': 'Minsk', 't_out': '19:40:00', 'st_in': 'SPB', 't_in': '6:14:00'},
              {'train_number': 1003, 'st_out': 'Minsk', 't_out': '14:51:00', 'st_in': 'Omsk', 't_in': '19:45:00'},
              {'train_number': 1004, 'st_out': 'Minsk', 't_out': '23:30:00', 'st_in': 'Tyla', 't_in': '19:45:00'},
              {'train_number': 1005, 'st_out': 'Minsk', 't_out': '17:30:00', 'st_in': 'Brest', 't_in': '20:54:00'},
              ]

for i in dictionary:
    tdelta = datetime.datetime.strptime(str(i['t_in']), '%H:%M:%S') - datetime.datetime.strptime(str(i['t_out']), '%H:%M:%S')
    if tdelta.days < 0:
        tdelta = datetime.timedelta(days=0, seconds=tdelta.seconds, microseconds=tdelta.microseconds)
    if datetime.datetime.strptime(str(tdelta), '%H:%M:%S') > datetime.datetime.strptime('7:20:00', '%H:%M:%S'):
        print(i)

