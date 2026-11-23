file_name = input("Enter the file name:")

try:
    file = open(file_name, "r")
    content = file.read()
    file.close()

    if content == "":
        print("The file is empty")
    else:
        print(content)
except FileNotFoundError:
    print("The file was not found")