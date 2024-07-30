file = open('dane3.txt', 'r')
ranges = []
longest = 0

for line in file:
    line = line.split()
    ranges.append(line)

for i in range(len(ranges)):
    first_range = ranges[i]
    longest_temp = 1
    for j in range(1, len(ranges)):
        next_range = ranges[j]
        if first_range[0] <= next_range[0] and first_range[1] <= next_range[1]:
            longest_temp += 1
        else:
            if longest_temp > longest:
                longest = longest_temp
            break

print(longest)

file.close()
