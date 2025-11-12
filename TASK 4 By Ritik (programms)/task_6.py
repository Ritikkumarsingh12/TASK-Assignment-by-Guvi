              #find duplicates in three list 
                       
#here we have given the three lists
list1 = [8,4,5,6,1]
list2 = [7,4,2,3,6]
list3 = [10,8,7,4,1]

common_items = set(list1) & set(list2) & set(list3)

# Print the duplicates present in  lists
print("Common elements in all three lists:", list(common_items))
