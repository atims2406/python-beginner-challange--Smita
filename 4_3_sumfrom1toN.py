n = int(input("Enter N: "))
total = 0

for number in range(1, n + 1):
    total = total + number

print("Sum of numbers from 1 to", n, "is", total)