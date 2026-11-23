students = []


def make_student(roll, name, m1, m2, m3):
    student = {"roll": roll, "name": name, "m1": m1, "m2": m2, "m3": m3}
    return student


def make_line(s):
    line = s["roll"] + "," + s["name"] + "," + str(s["m1"]) + "," + str(s["m2"]) + "," + str(s["m3"])
    return line


def load_students():
    try:
        file = open("students.txt", "r")
        for line in file:
            line = line.strip()
            parts = line.split(",")
            student = make_student(parts[0], parts[1], float(parts[2]), float(parts[3]), float(parts[4]))
            students.append(student)
        file.close()
    except FileNotFoundError:
        print("No saved file yet")


def save_students():
    file = open("students.txt", "w")
    for s in students:
        file.write(make_line(s) + "\n")
    file.close()


def find_student(roll):
    for s in students:
        if s["roll"] == roll:
            return s
    return None


def print_student(s):
    print(s["roll"], s["name"], s["m1"], s["m2"], s["m3"])


def get_average(s):
    total = s["m1"] + s["m2"] + s["m3"]
    return total / 3


def add_student():
    roll = input("Enter roll number: ")
    name = input("Enter name: ")
    try:
        m1 = float(input("Enter marks 1: "))
        m2 = float(input("Enter marks 2: "))
        m3 = float(input("Enter marks 3: "))
    except ValueError:
        print("Marks must be numbers. Student not added.")
        return
    student = make_student(roll, name, m1, m2, m3)
    students.append(student)
    save_students()
    print("Student added")


def view_students():
    if len(students) == 0:
        print("No students found")
    for s in students:
        print_student(s)


def search_student():
    roll = input("Enter roll number: ")
    s = find_student(roll)
    if s == None:
        print("Student not found")
    else:
        print_student(s)


def average_marks():
    roll = input("Enter roll number: ")
    s = find_student(roll)
    if s == None:
        print("Student not found")
    else:
        print("Average marks of", s["name"], "is", round(get_average(s), 2))


def show_menu():
    print()
    print("1. Add student")
    print("2. View all students")
    print("3. Search student by roll number")
    print("4. Calculate average marks")
    print("5. Exit")


load_students()

while True:
    show_menu()
    choice = input("Enter your choice: ")

    if choice == "1":
        add_student()
    elif choice == "2":
        view_students()
    elif choice == "3":
        search_student()
    elif choice == "4":
        average_marks()
    elif choice == "5":
        print("Goodbye")
        break
    else:
        print("Wrong choice")