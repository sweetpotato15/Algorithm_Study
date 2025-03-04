command = input().strip()
command = command.replace('()', 'R')
answer = 0

left, right = 0, 0
for i in range(len(command)):
    if command[i] == '(':
        left += 1
    elif command[i] == ')':
        right += 1
    else:
        answer += left-right

answer += command.count(')')

print(answer)