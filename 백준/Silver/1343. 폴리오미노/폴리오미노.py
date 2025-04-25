string = input().strip().split('.')
answer = []
for i in string:
    if len(i)%2 ==1:
        print(-1)
        exit()
    elif len(i)%4==2:
        answer.append('A'*(len(i)-2)+'BB')
    else:
        answer.append('A'*len(i))

print('.'.join(answer))