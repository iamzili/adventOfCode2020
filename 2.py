import re

passworld_list = []
first_valid = 0
second_valid = 0

with open('2_input') as f:
    passworld_list = [line.rstrip() for line in f]


for x in passworld_list:
    # remove chars "-" ":" then split
    # e.g: [2, 6, 'p', 'gpwhqpbpgdrprbbp']
    line = [int(y) if y.isdigit() else y for y in re.sub("-|:", " ", x).split()]
    char_count = line[3].count(line[2])

    if line[0] <= char_count <= line[1]:
        first_valid += 1

    if (line[3][line[0] - 1] == line[2]) != (line[3][line[1] - 1] == line[2]):
        second_valid += 1

print(f'The number of first_valid password is: {first_valid}')
print(f'The number of second_valid password is: {second_valid}')
