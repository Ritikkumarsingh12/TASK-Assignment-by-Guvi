
#find prime numbers and count 

#here we have takes the data list 
data_list = [10, 501, 22, 37, 100, 999, 87, 351]

#here we are checking the prime numbers using the if condition & using for loop
def check_prime(number):
    if number < 2:
        return False
    for divisor in range(2, int(number**0.5) + 1):
        if number % divisor == 0:
            return False
    return True

prime_list = [number for number in data_list if check_prime(number)]
#here we are printing the prime number & list 
print("Prime Numbers:", prime_list)
print("Total Prime Numbers:", len(prime_list))
