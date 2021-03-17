import re

with open('4_input') as f:
    batch_file = [line.rstrip() for line in f]
batch_file.append("")

fields = ['byr','iyr','eyr','hgt','hcl','ecl','pid']
valid_ecl = ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']
passport = ""
num_valid_passports_1 = 0
num_valid_passports_2 = 0

def validate(passport, field):
    if field in passport:
        value = passport.split(field + ':')[1].split()[0]
        if field == 'byr':
            if 1920 <= int(value) <= 2002:
                return 1
        elif field == 'iyr':
            if 2010 <= int(value) <= 2020:
                return 1
        elif field == 'eyr':
            if 2020 <= int(value) <= 2030:
                return 1
        elif field == 'hgt':
            if 'cm' in value:
                if 150 <= int(value.split('cm')[0]) <= 193:
                    return 1
            elif 'in' in value:
                if 59 <= int(value.split('in')[0]) <= 76:
                    return 1
        elif field == 'hcl':
            if bool(re.match('^#{1}[0-9a-f]{6}$', value)):
                return 1
        elif field == 'ecl':
            if value in valid_ecl:
                return 1
        elif field == 'pid':
            if bool(re.match('^[0-9]{9}$', value)):
                return 1
        elif field == 'cid':
                return 1
        else:
            return 0
    else:
        return 0

for x in batch_file:
    passport += x + " "
    if not x:
        # part1 - generator expression
        if all(x in passport for x in fields):
            num_valid_passports_1 += 1
        # part 2
        if all(validate(passport,x) for x in fields):
            num_valid_passports_2 += 1
        passport = ""


print(f'Number of valid passports for Part 1: {num_valid_passports_1}')
print(f'Number of valid passports for Part 2: {num_valid_passports_2}')




