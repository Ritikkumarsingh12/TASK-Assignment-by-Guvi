              #Extract Year, Month, Day using lambda

from datetime import datetime

# Current date and time stored in a variable
current_date = datetime.now()

# here we have used lamda function 
get_ymd = lambda d: (d.year, d.month, d.day)

# Printing the output (means date,time,year)
print(get_ymd(current_date))  
