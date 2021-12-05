from datetime import datetime
import argparse
import time


parser = argparse.ArgumentParser()
parser.add_argument('-f', '--family')
parser.add_argument('-hh', '--hours', default=0, type=int)
parser.add_argument('-m', '--minutes', default=1, type=int)
parser.add_argument('-s', '--seconds', default=5, type=int)
args = parser.parse_args()
print(args)

with open('log.txt', 'a') as file:
    file.write(f'{datetime.now().strftime("%d/%m/%y %H:%M:%S")} - {args.family} \n')
while args.hours or args.minutes or args.seconds:
    show_time_str = ''
    if args.hours < 10:
        show_time_str += f'0{args.hours}'
    else:
        show_time_str += f'{args.hours}'

    if args.minutes < 10:
        show_time_str += f':0{args.minutes}'
    else:
        show_time_str += f':{args.minutes}'

    if args.seconds < 10:
        show_time_str += f':0{args.seconds}'
    else:
        show_time_str += f':{args.seconds}'
    print(show_time_str)
    time.sleep(1)
    if args.seconds == 0 and args.minutes > 0:
        args.minutes -= 1
        args.seconds = 59
    elif args.seconds == 0 and args.minutes == 0 and args.hours > 0:
        args.hours -= 1
        args.minutes = 59
        args.seconds = 59
    else:
        args.seconds -= 1
else:
    print('ALARM!!!!')
