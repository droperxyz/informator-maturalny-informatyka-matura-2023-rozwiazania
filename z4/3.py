file = open('dane4.txt', 'r')

nums_list = []
highest_i = 0
max_pairs = 0

for line in file:
    line = int(line.strip())
    nums_list.append(line)

for i in range(len(nums_list)):
    pairs = 0
    for j in range(i):
        if nums_list[i] > nums_list[j]:
            pairs += 1
    if pairs > max_pairs:
        max_pairs = pairs
        highest_i = i
    
print(highest_i + 1, max_pairs)
    
file.close()
