              #___Separate Even and Odd Numbers____


#here is the given list of numbers 
numbers = [10, 501, 22, 37, 100, 999, 87, 351]

#here we have created two empty lists to store even and odd numbers 
even_list = []
odd_list = []

for num in numbers:
    if num % 2 == 0:            #it will check that number is even if devided by 2
        even_list.append(num)
    else:
        odd_list.append(num)

#here it will print even and odd number
print("Even Numbers:", even_list)
print("Odd Numbers:", odd_list)
