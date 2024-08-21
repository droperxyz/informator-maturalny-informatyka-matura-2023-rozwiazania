def IsPalindrome(s):
    n = len(s)
    for i in range(n // 2):
        if s[i] == s[n-i-1]:
            return True
    
    return False

file = open("dane6.txt", "r")
counter = 0

for line in file:
    line = line.strip()
    if not IsPalindrome(line):
        print(line)
        counter += 1

print(counter)

file.close()
