import argparse
from datetime import datetime


parser = argparse.ArgumentParser()
parser.add_argument('-f', '--family')
parser.add_argument('-mm', '--minutes', default=25, type=int)
parser.add_argument('-ss', '--seconds', default=0, type=int)
parser.add_argument('-ps', '--pause_minutes', default=5, type=int)
parser.add_argument('-nc', '--number_cycles', default=4, type=int)
parser.add_argument('-nt', '--name_task', type=str)
args = parser.parse_args()
with open('log.txt', 'a') as file:
    file.write(f'{datetime.now().strftime("%d/%m/%y %H:%M:%S")} - {args.family}, '
               f'{args.minutes} min, pause {args.pause_minutes} min, '
               f'{args.number_cycles} cycles, {args.name_task} \n')
