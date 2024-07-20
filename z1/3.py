highest_sum = -101
file = open('dane1_3.txt', 'r')
nums=[]

for digit in file:
    digit = digit.strip()
    nums.append(digit)

for i in range(len(nums)):
    temp = 0
    for j in range(i, len(nums)):
        temp += int(nums[j])

        if temp > highest_sum:
            highest_sum = temp

print(highest_sum)
