#!/usr/bin/env python3

# erase specific char from string (a-z + A-Z + ' ')
import re
str="Hello, World!"
str=re.sub(r'[^a-zA-Z ]+', '', str)
print(str)
