text = input("Enter some text: ")

file = open("notes.txt", "w")
file.write(text)
file.close()

print("Your text is saved in notes.txt")

file = open("notes.txt", "r")
content = file.read()
file.close()

print("The file contains:")
print(content)