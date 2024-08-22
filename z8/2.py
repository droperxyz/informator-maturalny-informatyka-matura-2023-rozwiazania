file = open("dane8.txt", "r")

numbers = []
counter = 0

for line in file:
    line = line.strip()
    numbers.append(int(line))

for i in range(len(numbers)):
    testing = numbers[i]
    for j in range(i, len(numbers)):
        if testing > numbers[j]:
            counter += 1

print(counter)

file.close()
