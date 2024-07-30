file = open('dane3.txt', 'r')
ranges = []

def GetRangeLen(a, b):
    return b - a + 1

for i in range(2024):
    ranges.append(0)


for line in file:
    line = line.split()
    a = int(line[0])
    b = int(line[1])
    range_len = GetRangeLen(a, b)
    ranges[range_len] += 1

print(ranges.index(max(ranges)))

file.close()
