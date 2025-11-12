
# Program to find triplet with a given sum

numbers = [10, 20, 30, 9]
sum = 59

found = False
n = len(numbers)

for i in range(n):
    for j in range(i + 1, n):
        for k in range(j + 1, n):
            if numbers[i] + numbers[j] + numbers[k] == sum:
                print("Triplet found:", numbers[i], numbers[j], numbers[k])
                found = True

if not found:
    print("triplet not found with the given sum.")
