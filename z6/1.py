def CheckIfPMinimal(p, number):
    checker = p - 1
    for i in range(len(number)):
        if int(number[i]) > checker:
            return False
    return str(checker) in number
        

file = open("dane6.txt", "r")
p_minimal_counter = [0] * 11

for line in file:
    line = line.strip()
    for p in range(2, 11):
        if CheckIfPMinimal(p, line):
            p_minimal_counter[p] += 1

print(p_minimal_counter[2:])

file.close()
