# Map : map(function_to_apply, list_of_inputs)
items = [1, 2, 3, 4, 5]
squared = list(map(lambda x: x**2, items))

# Filter
number_list = range(-5, 5)
less_than_zero = list(filter(lambda x: x < 0, number_list))
print(less_than_zero)

# Reduce
from functools import reduce
product = reduce((lambda x, y: x * y), [1, 2, 3, 4])
