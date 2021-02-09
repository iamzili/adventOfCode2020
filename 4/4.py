with open('4_input') as f:
    batch_file = [line.rstrip() for line in f]
batch_file.append("")

fields = ['byr','iyr','eyr','hgt','hcl','ecl','pid']
passport = ""
num_valid_passports = 0

for x in batch_file:
    passport += x + " "
    if not x:
        if all(x in passport for x in fields):
            num_valid_passports += 1
        passport = ""

print(f'Number of valid passports {num_valid_passports}')



