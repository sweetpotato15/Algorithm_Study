# 백준 20125 쿠키의 신체 측정
import sys
input = sys.stdin.readline

# 심장의 위치를 구하고 
n = int(input())
cookie = []
head_row = n+1 

for i in range(1,n+1):
    word = input().strip()
    cookie.append(word)
    if word.count('*') != 0:
        head_row = min(head_row, i)
        head_col = cookie[head_row-1].index('*') + 1


heart = [head_row + 1, head_col]
left_arm = heart[1] - cookie[heart[0]-1].index('*') -1
right_arm = n - cookie[heart[0]-1][::-1].index('*') - heart[1]

bone = 0
left_leg = 0
right_leg = 0
for i in range(heart[0], n):
    if cookie[i][heart[1]-1] == '*':
        bone += 1
    if cookie[i][heart[1]-2] == '*':
        left_leg += 1
    if cookie[i][heart[1]] == '*':
        right_leg += 1


print(*heart)
print(left_arm, right_arm, bone, left_leg, right_leg)




