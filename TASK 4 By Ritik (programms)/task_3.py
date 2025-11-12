
#find how many happy numbers are in list 

#here we have taken out data list 
numbers = [10, 501, 22, 37, 100, 999, 87, 351]

#here we are writting the logic for happy numbers 
def is_happy(num):
    seen = set()
    while num != 1 and num not in seen:
        seen.add(num)
        num = sum(int(digit)**2 for digit in str(num))
    return num == 1

happy_numbers = [n for n in numbers if is_happy(n)]

#here we are printing the happy numbers
print("Happy Numbers are:", happy_numbers)
print("Total Happy Numbers:", len(happy_numbers))
