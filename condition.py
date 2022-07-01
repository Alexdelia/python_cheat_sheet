#!/usr/bin/env python3

# (condition ? true : false)
# x = (x > y ? x : y)   // max
# [false, true][condition]

x=21;y=42

x = [y, x][x > y]

print(x)
