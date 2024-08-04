def CheckIfPMinimal(p, number):
    checker = p - 1
    for i in range(len(number)):
        if int(number[i]) > checker:
            return False
    return str(checker) in number
        

file = open("dane6.txt", "r")
biggest_sum = [0] * 11
numbers = [0] * 11
for line in file:
    line = line.strip()
    for p in range(2, 11):
        if CheckIfPMinimal(p, line):
            sum_of_nums = 0
            for digit in line:
                sum_of_nums += int(digit)
            if sum_of_nums > biggest_sum[p]:
                biggest_sum[p] = sum_of_nums
                numbers[p] = line

for i in range(2, len(numbers)):
    print(i)
    print(numbers[i])
             
file.close()
