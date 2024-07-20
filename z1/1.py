a = [2, -3, 1, -7, 4, -2, -1, 5, -3, 2, -1]

biggest_sum = -9999999
for i in range(len(a)):
    temp = a[i]
    for j in range(i+1, len(a)):
        temp += a[j]

        if temp > biggest_sum:
            biggest_sum = temp
            start = i
            end = j

print(a[start], a[end])
