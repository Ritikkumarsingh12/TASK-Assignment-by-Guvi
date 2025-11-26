         #Squares of even numbers using list comprehension + lambda

#here we have gave the Input number list
numbers = [1, 2, 3, 4, 5, 6]

# Lambda to check even number
check_even = lambda n: n % 2 == 0

# here we are Create a list of squares for even numbers 
even_square_list = [n * n for n in numbers if check_even(n)]

# Printing  the result
print(even_square_list)
