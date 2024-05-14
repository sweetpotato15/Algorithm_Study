import sys
input = sys.stdin.readline
from collections import deque

left = deque(list(input().strip()))
right = deque([])
n = int(input())
 
for i in range(n):
    command = input().strip()
    if command[0] == 'P':
        left.append(command[2:])
    elif command[0] == 'L':
        if left:
            right.appendleft(left.pop())
    elif command[0] == 'D':
        if right:
            left.append(right.popleft())
    else:
        if left:
            left.pop()

print(''.join(left+right))