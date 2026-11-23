names = ["Smita", "Eeshika", "Priesha", "Kabir", "Sana"]

search = input("Enter a name to search: ")

if search in names:
    print(search, "is in the list")
else:
    print(search, "is not in the list")