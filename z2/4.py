file = open('dane2_4.txt', 'r')

for line in file:
    line = line.strip()
    
    opening_brackets = 0
    closing_brackets = 0

    for char in line:
        if char == "[":
            opening_brackets += 1
        else:
            closing_brackets += 1
    
    if opening_brackets == closing_brackets:
        print('tak')
    else:
        print('nie')

file.close()
