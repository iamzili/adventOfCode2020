from os import path

basedir = path.abspath(path.dirname(__file__))

part1 = 0
part2 = 0

with open(f'{basedir}/day_3_input') as f:
    my_map = [line.rstrip() for line in f]


def calc_trees(step_right, step_down):
    right = 0
    down = 0
    num_tree = 0
    num_pattern = 1

    # [1:] skip first iteration
    for x in my_map[1:]:
        down += 1
        if down < step_down:
            continue

        right += step_right
        try:
            if x[right] == "#": 
                num_tree += 1
        except:
            num_pattern += 1
            x = num_pattern * x
            if x[right] == "#": 
                num_tree += 1
        down = 0

    return num_tree


part1 = calc_trees(3,1)
part2 = calc_trees(1,1) * calc_trees(3,1) * calc_trees(5,1) * calc_trees(7,1) * calc_trees(1,2)
print(f'Part one - number of trees: {part1}')
print(f'Part two - number of trees: {part2}')