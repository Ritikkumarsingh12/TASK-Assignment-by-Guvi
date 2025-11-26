          # Lambda function to check if a string is numeric or not 

check_number = lambda text: text.replace('.', '', 1).isdigit()

# Testing output
print(check_number("123"))     
print(check_number("45.67"))   
print(check_number("hello"))   
