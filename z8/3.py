file = open("dane8.txt", "r")

numbers = []
highest_len = 0
length = 1

for line in file:
    line = line.strip()
    numbers.append(int(line))

for i in range(len(numbers)-1):
    if numbers[i] < numbers[i+1]:
        length += 1
    else:
        if length > highest_len:
            highest_len = length
        length = 1

print(highest_len)

file.close()
