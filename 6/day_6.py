#!/usr/bin/env python

from os import path
from collections import OrderedDict

basedir = path.abspath(path.dirname(__file__))

first_part = second_part = 0

def remove_duplicate(string: str) -> str:
  return "".join(OrderedDict.fromkeys(string))

with open(f"{basedir}/day_6_input", "r") as f:
    content = f.read().split("\n\n")

for i in content:
    group = i.split('\n')
    listToStr = ''.join(map(str, group))
    first_part += int(len(remove_duplicate(listToStr)))

    answer = group[0]
    for x in group[1:]:
        answer = set(answer).intersection(x)
    second_part += int(len(answer))
    

print(f"First part: {first_part}")
print(f"Second part: {second_part}")

