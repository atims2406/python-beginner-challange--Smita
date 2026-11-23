marks = []

for i in range(5):
    mark = int(input("Enter marks: "))
    marks.append(mark)

total = sum(marks)
average = total / 5

print("Total:", total)
print("Average:", average)
print("Highest:", max(marks))
print("Lowest:", min(marks))