          #Filter out people under 18

# here we suppose the  List of dictionaries 
people_list = [
    {"name": "Ritik", "age": 25},
    {"name": "Kartik", "age": 36},
    {"name": "kavita", "age": 14},
    {"name": "priya", "age": 17}
]

# her we are filtering the people whose age is 18 or above 
only_adults = list(filter(lambda person: person['age'] >= 18, people_list))

# here we extracting the name
adult_names = list(map(lambda person: person['name'], only_adults))

# Print the output
print(adult_names)
