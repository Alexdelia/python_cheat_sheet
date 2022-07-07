#!/usr/bin/env python3

# one line loop
s="01234"
S="ABC"
[print(x, y) for x in s for y in S]

print()
# palindrome
p="abccba"
P="abcba"
n="hello"
print(p == p[::-1])
print(P == P[::-1])
print(n == n[::-1])
