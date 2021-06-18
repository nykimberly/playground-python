# -*- coding: utf-8 -*-

from fractions import Fraction

f1 = Fraction(1, 2)
f2 = Fraction(1, 6)
f3 = Fraction(1, 2)
print("f1 is", f1, sep=" ", end=".\n")
print("f2 is", f2, sep=" ", end=".\n")
print("f3 is", f3, sep=" ", end=".\n")
print("f1 == f2 is", f1 == f2, sep=" ", end=".\n")
print("f1 == f3 is", f1 == f3, sep=" ", end=".\n")
print("f1 + f2 is", f1 + f2, sep=" ", end=".\n")
print("f1 - f2 is", f1 - f2, sep=" ", end=".\n")
print("f1 * f2 is", f1 * f2, sep=" ", end=".\n")
print("f1 / f2 is", f1 / f2, sep=" ", end=".\n")
