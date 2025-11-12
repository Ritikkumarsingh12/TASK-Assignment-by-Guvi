# Program to check if there is a sub-list with sum equal to zero


#her is the given list 
numbers = [4, 2, -3, 1, 6]
found = False

# Loop through all possible sub-lists
for i in range(len(numbers)):
    for j in range(i, len(numbers)):
        # Check the sum of current sub-list
        if sum(numbers[i:j+1]) == 0:
            print("Sub-list with sum 0 found:", numbers[i:j+1])
            found = True
            break
    if found:
        break

if not found:
    print("No sub-list found with sum equal to zero.")
