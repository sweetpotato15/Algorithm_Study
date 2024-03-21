X, Y = map(int, input().split()) # X : 가로 길이, Y : 세로 길이
cut = int(input())

y_input = [0,Y] # 잘리는 y 좌표들
x_input = [0,X] # 잘리는 x 좌표들

for i in range(cut):
    a,b = map(int, input().split())
    if a == 0:
        y_input.append(b)
    else:
        x_input.append(b)

x_input.sort()
y_input.sort()

answer = 0

for i in range(len(x_input)-1):
    for j in range(len(y_input)-1):
        answer = max(answer, (x_input[i+1]-x_input[i]) * (y_input[j+1] - y_input[j]))

print(answer)