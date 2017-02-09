file = open("text3", "r")
alphabet = dict()
for line in file:
    for char in line:
        if char.lower() not in alphabet:
            alphabet[char.lower()] = 0
        else:
            alphabet[char.lower()] += 1
alphabet = sorted(alphabet.items(), key=lambda x: x[1], reverse=True)
print(alphabet)