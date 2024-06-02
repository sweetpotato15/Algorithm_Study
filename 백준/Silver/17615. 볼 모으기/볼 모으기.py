import sys
input = sys.stdin.readline
from collections import deque

n = int(input())
string = input().strip()

count = []
# 1) 빨을 좌측으로
c = 0
answer = 0
for i in range(n-1,-1,-1):
    if string[i] == 'R':
        c += 1
    elif string[i] == 'B' and c > 0 :
        answer += c
        c = 0
count.append(answer)

# 2) 빨을 우측으로
c = 0
answer = 0
for i in range(n):
    if string[i] == 'R':
        c += 1
    elif string[i] == 'B' and c>0:
        answer += c
        c = 0
count.append(answer)

# 3) 파를 좌측으로 
c = 0
answer = 0
for i in range(n-1,-1,-1):
    if string[i] == 'B':
        c += 1
    elif string[i] == 'R' and c > 0 :
        answer += c
        c = 0
count.append(answer)

# 4) 파를 우측으로 
c = 0
answer = 0
for i in range(n):
    if string[i] == 'B':
        c += 1
    elif string[i] == 'R' and c>0:
        answer += c
        c = 0
count.append(answer)

print(min(count))