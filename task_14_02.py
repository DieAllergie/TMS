import argparse
from datetime import datetime
import time


parser = argparse.ArgumentParser()
parser.add_argument('-f', '--family')
parser.add_argument('-mm', '--minutes', default=2, type=int)
# parser.add_argument('-ss', '--seconds', default=0, type=int)
parser.add_argument('-ps', '--pause_minutes', default=1, type=int)
parser.add_argument('-nc', '--number_cycles', default=2, type=int)
parser.add_argument('-nt', '--name_task', type=str)
args = parser.parse_args()
with open('log.txt', 'a') as file:
    file.write(f'{datetime.now().strftime("%d/%m/%y %H:%M:%S")} - {args.family}, '
               f'{args.minutes} min, pause {args.pause_minutes} min, '
               f'{args.number_cycles} cycles, {args.name_task} \n')

time_work = args.minutes
while time_work or args.number_cycles:
    if time_work > 0:
        print(f'Left to work: {time_work} min.')
        time.sleep(60)
        time_work -= 1
    elif time_work == 0 and args.number_cycles > 0:
        print(f'Your activity time has expired. You have a {args.pause_minutes} minute break')
        time.sleep(args.pause_minutes * 60)
        args.number_cycles -= 1
        time_work = args.minutes
print('Your task and!!!')
