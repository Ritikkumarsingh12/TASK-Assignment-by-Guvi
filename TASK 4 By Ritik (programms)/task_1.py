              #___Separate Even and Odd Numbers____

numbers_list = [10, 501, 22, 37, 100, 999, 87, 351]

even_list = [value for value in numbers_list if value % 2 == 0]
odd_list = [value for value in numbers_list if value % 2 != 0]

print("Even Numbers:", even_list)
print("Odd Numbers:", odd_list)
