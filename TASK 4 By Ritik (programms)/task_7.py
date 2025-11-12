
                 #find the non repeating element

# here we have given the  list of numbers
numbers = [10, 501, 22, 37, 100, 999, 87, 351, 22, 37, 10]

for num in numbers:
    #It will Check if the number appears only once
    if numbers.count(num) == 1:
        print("First non-repeating element:", num)
        break  
    #it will Stop after finding the first one
