import sys
from os import path
from itertools import combinations 

basedir = path.abspath(path.dirname(__file__))

expenses_list = []

f = open(f"{basedir}/day_1_input",'r',encoding = 'utf-8')
for line in f:
    expenses_list.append(int(line))

#List comprehensions 
first_part = [x for x in list(combinations(expenses_list, 2)) if sum(x) == 2020][0]
part1 = first_part[0] * first_part[1]
print(f'first solution: {part1}')

second_part = [x for x in list(combinations(expenses_list, 3)) if sum(x) == 2020][0]
part2 = second_part[0] * second_part[1] * second_part[2]
print(f'second solution: {part2}')
