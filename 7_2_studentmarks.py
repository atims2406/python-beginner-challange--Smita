name = input("Enter student name: ")
marks = input("Enter marks: ")

file = open("student.txt", "w")
file.write("Name: " + name + "\n")
file.write("Marks: " + marks + "\n")
file.close()

print("Your file is saved in student.txt")

file = open("student.txt", "r")
print(file.read())
file.close()