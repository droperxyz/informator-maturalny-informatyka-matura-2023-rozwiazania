highest_sum = -101
file = open('dane1_4.txt', 'r')
current_sum = 0
starting_point = 0
end_point = 0
temp_starting_point = 0

for i, digit in enumerate(file):
    digit = int(digit.strip())

    if current_sum > 0:
        current_sum += digit
    else:
        current_sum = digit
        temp_starting_point = i

    if current_sum > highest_sum:
        highest_sum = current_sum
        starting_point = temp_starting_point
        end_point = i

print(starting_point + 1, end_point + 1)
