
#sum of ist and last digit

#here we are taking the input prom the user 
user_number = int(input("Enter a number: "))
# Convert the number to string to access digits
number_str = str(user_number)
digit_sum = int(number_str[0]) + int(number_str[-1])
# Print the result
print("Sum of first and last digit:", digit_sum)
