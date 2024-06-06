string = input().strip()

num_a = string.count('a')
new_s = string[:] + string[:]
# aaabba a가 4개 이므로 index 0 ~ 2 까지 반복
maximum = 0
for i in range(0,len(new_s)-num_a+1):
    maximum = max(maximum, new_s[i:i+num_a].count('a'))

print(num_a - maximum)