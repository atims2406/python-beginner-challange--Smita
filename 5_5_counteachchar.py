text = input("Enter some text:")
counts = {}

for character in text:
    if character in counts:
        counts[character]=counts[character] + 1
    else:
        counts[character]=1

for character in counts:
    print(character, ":", counts[character])