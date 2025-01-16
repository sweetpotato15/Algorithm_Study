answer = 0
for i in range(8):
    command = list(input())
    if i % 2 == 0:
        answer += command[::2].count('F')
    else:
        answer += command[1::2].count('F')
print(answer)