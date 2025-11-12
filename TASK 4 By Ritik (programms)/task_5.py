
#finding the all ways to make the rupees 10 by using 1,2,5 rupees

# We will try all possible counts of Rupees1,2,5 
for one_rup in range(11):     
    for two_rup in range(6):  
        for five_rup in range(3):  
            # Check if total value is exactly 10 rupees
            if one_rup * 1 + two_rup * 2 + five_rup * 5 == 10:
                print(f"1Rup coins: {one_rup}, 2Rup coins: {two_rup}, 5rup coins: {five_rs}")
