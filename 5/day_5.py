#!/usr/bin/env python

#python3 day_5.py day_5_input
import fileinput

t = str.maketrans("FBLR", "0101")
s = set(int(l.translate(t), 2) for l in fileinput.input())
lo, hi = min(s), max(s)

print(hi)
missing = next(i for i in range(lo + 1, hi) if i not in s)
print(missing)