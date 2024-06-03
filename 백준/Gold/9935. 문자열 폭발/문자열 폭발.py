import sys
input = sys.stdin.readline

string = str(input().strip())
target = list(input().strip())
n = len(target)
stack = []

for i in string:
    stack.append(i)
    while len(stack) >= n and stack[-n:] == target:
        del stack[-n:]
if stack: print(''.join(stack))
else: print('FRULA')
        