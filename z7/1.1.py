file = open("szyfrogram.txt", "r")

letters_counter = {}

for line in file:
    line = line.strip()

    for letter in line:
        if letter in letters_counter:
            letters_counter[letter] += 1
        else:
            letters_counter[letter] = 1

sorted_letters = sorted(letters_counter.items())

for i in range(len(sorted_letters)):
     print(sorted_letters[i][0] + " " + str(sorted_letters[i][1]))

