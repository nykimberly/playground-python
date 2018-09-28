import re

location = """
Washington D.C., DC, USA
"""

match = re.search(r'(\w+)\s(D\.C\.), (\w\w)\W', location).groups()
print(match) #('Washington', 'D.C.', 'DC')
match = re.search(r'(\w+)\s(?:D\.C\.), (\w\w)\W', location).groups()
print(match) # ('Washington', 'DC')
