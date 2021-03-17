import re
from os import path

basedir = path.abspath(path.dirname(__file__))

passworld_list = []
part1 = 0
part2 = 0

with open(f'{basedir}/day_2_input') as f:
    passworld_list = [line.rstrip() for line in f]


for x in passworld_list:
    # line = [2, 6, 'p', 'gpwhqpbpgdrprbbp']
    line = [int(y) if y.isdigit() else y for y in re.sub("-|:", " ", x).split()]
    char_count = line[3].count(line[2])

    if line[0] <= char_count <= line[1]:
        part1 += 1

    if (line[3][line[0] - 1] == line[2]) ^ (line[3][line[1] - 1] == line[2]):
        part2 += 1

print(f'The number of part1 password is: {part1}')
print(f'The number of part2 password is: {part2}')
