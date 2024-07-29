file = open('dane3.txt', 'r')

min1 = float('inf')
min2 = float('inf')

def GetRangeLen(a, b):
    return b - a + 1

for line in file:
    line = line.split()
    a = int(line[0])
    b = int(line[1])
    range_len = GetRangeLen(a, b)

    if range_len < min1:
        min2 = min1
        min1 = range_len
    elif range_len < min2:
        min2 = range_len
   
print(min1, min2)

file.close()
