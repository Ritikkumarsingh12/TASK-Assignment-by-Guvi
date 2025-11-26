       
 # Generate Fibonacci series using lambda


from functools import reduce

# here we usdd Lambda function to generate Fibonacci series up to n terms
make_fib = lambda count: reduce(
    lambda seq, _: seq + [seq[-1] + seq[-2]], 
    range(count - 2),
    [0, 1]
)

# Print first 10 Fibonacci numbers
print(make_fib(10))
