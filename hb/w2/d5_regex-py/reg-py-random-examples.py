import re

input_text = """
hello
a
b
ab a b a#b
14155551212
4155551212
JavaScript Java Script
Yy Yay Yaaaaaaay
I like cats I like dogs
415-555-1212 4-5-1
Call:14155551212
San Francisco info Call:   415-555-1212
6198088974
619 808 9295
1-858-808-8974
"""
regex_exp = []
regex_exp.append("hello")
regex_exp.append("a\sb")
regex_exp.append("[aeiou]")
regex_exp.append("[a-f]")
regex_exp.append("[a.b]")
regex_exp.append("1?4155551212")
regex_exp.append("Java ?Script")
regex_exp.append("Call:\s*\d*")
regex_exp.append("(I like {catdog)s)")
regex_exp.append("Ya+y")
regex_exp.append("Ya*y")
regex_exp.append("[a*b]")
regex_exp.append("(\d{3})")
regex_exp.append("(\d{3})?-?(\d{3}-?\d{4})")

for i, exp in enumerate(regex_exp):
    print(f"\npattern #{i}: {exp}")
    PHONE_REG = re.compile(exp)
    print(re.findall(PHONE_REG, input_text))
