import sys
from itertools import combinations  

expenses_list = []

f = open("1_input",'r',encoding = 'utf-8')
for line in f:
    expenses_list.append(int(line))

first_part = [x for x in list(combinations(expenses_list, 2)) if sum(x) == 2020][0]
print(f'first solution: {first_part[0] * first_part[1]}')

second_part = [x for x in list(combinations(expenses_list, 3)) if sum(x) == 2020][0]
print(f'second solution: {second_part[0] * second_part[1] * second_part[2]}')
