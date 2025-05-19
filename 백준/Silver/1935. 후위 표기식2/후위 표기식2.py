import sys
input = sys.stdin.readline
from collections import deque

N = int(input())
formula = input().strip()
q = deque([]) 
dict = {}

for i in range(N):
    dict[chr(65+i)] = int(input())

for i in formula:
    if 65 <= ord(i) <= 90:
        q.append(dict[i])
    else:
        num2 = str(q.pop())
        num1 = str(q.pop())
        q.append(eval(f'{num1}{i}{num2}'))

print(f'{q.pop():.2f}')