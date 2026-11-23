def average(marks):
    total = sum(marks)
    return total / len(marks)


my_marks = []

print("Please enter 5 marks")

for i in range(1, 6):
    print("Marks", i, "of 5")
    mark = int(input())
    my_marks.append(mark)

print("Average marks:", average(my_marks))