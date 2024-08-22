file = open("szyfrogram.txt", "r")

letters = []
counter = [0] * 26

for i in range(65,91):
    letters.append(chr(i))

for line in file:
    line = line.strip()

    for letter in line:
        counter[ord(letter) - 65] += 1

for i in range(len(letters)):
    output = ""
    output += letters[i]
    output += str(counter[i])
    print(output)

file.close()
    
