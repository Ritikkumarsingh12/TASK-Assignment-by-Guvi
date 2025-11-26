            # Product of numbers using reduce + lambda

from functools import reduce

# here is the List of numbers
num_list = [9, 2, 1, 4]

# now Multiply all numbers in the list using reduce
result_product = reduce(lambda a, b: a * b, num_list)

# here output will Print 
print(result_product)
