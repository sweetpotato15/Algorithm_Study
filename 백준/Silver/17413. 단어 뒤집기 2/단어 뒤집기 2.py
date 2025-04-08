from collections import deque

q = deque(list(input().strip()))
stack = deque()
answer = ''
flag = False

for word in q:
    if word == '<':
        while stack:
            answer += stack.pop()
        flag = True
        stack.append(word)

    elif word == '>':
        while stack:
            answer += stack.popleft()
        flag = False
        answer += '>'
    
    elif word == ' ':
        if flag: # tag인 경우
            stack.append(word)
        else:
            while stack:
                answer += stack.pop()
            answer += ' '

    else:
        stack.append(word)

while stack:
    answer += stack.pop()
print(answer)
        