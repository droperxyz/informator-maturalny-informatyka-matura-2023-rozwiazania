file = open('dane2_3.txt', 'r')

for line in file:
    line = line.strip()
    depth = 0
    max_depth = 0
    
    for char in line:
        if char == "[":
            depth += 1
            if depth > max_depth:
                max_depth = depth
        else:
            depth -= 1
    
    print(max_depth)

file.close()
