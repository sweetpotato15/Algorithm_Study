import sys
input = sys.stdin.readline

N = int(input())
commands = []
for _ in range(N):
    string = list(input().strip())
    commands.append(tuple(string))

answer = ''

for i in list(zip(*commands)):
    if len(set(list(i))) == 1:
        answer += i[0]
    else:
        answer += "?"
print(answer)