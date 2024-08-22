file = open("dane8.txt", "r")
numbers = []
even = 0
odd = 0

for line in file:
    line = int(line.strip())
    numbers.append(line)

for i in range(1, len(numbers)):
    absolute = abs(numbers[i] - numbers[i-1])

    if absolute % 2 == 0:
        even += 1
    else:
        odd += 1

print(even, odd)

