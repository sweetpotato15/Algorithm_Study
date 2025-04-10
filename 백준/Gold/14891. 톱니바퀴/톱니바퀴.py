import sys
input = sys.stdin.readline
from collections import deque

graph = [deque(list(map(int, list(input().strip())))) for _ in range(4)]

K = int(input())
command = [list(map(int, input().split())) for _ in range(K)]

for num, d in command:
    rotate_lst = [0, 0, 0, 0] # 각 톱니바퀴가 회전할 방향
    rotate_lst[num-1] = d
    if num == 1 or num == 2:
        for i in range(num, 4): # 옆 톱니바퀴
            if graph[i-1][2] != graph[i][-2]:
                rotate_lst[i] = rotate_lst[i-1]*(-1)
            else:
                break

    elif num == 3 or num == 4:
        for i in range(num-6, -5, -1): # 옆 톱니바퀴
            if graph[i+1][-2] != graph[i][2]:
                rotate_lst[i] = rotate_lst[i+1]*(-1)    
            else:
                break
    
    if num == 2 and graph[0][2] != graph[1][-2]:
        rotate_lst[0] = rotate_lst[1]*(-1)
    if num == 3 and graph[2][2] != graph[3][-2]:
        rotate_lst[3] = rotate_lst[2]*(-1)

    for i in range(4):
        graph[i].rotate(rotate_lst[i])

answer = 0
for i in range(4):
    answer += 2**i*graph[i][0]
print(answer)
