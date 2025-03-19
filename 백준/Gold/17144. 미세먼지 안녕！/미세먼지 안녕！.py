import sys
input = sys.stdin.readline
from copy import deepcopy

def spread(graph):
    new_graph = [[0]*C for _ in range(R)]

    for i in range(R):
        for j in range(C):
            if graph[i][j]>0:
                count = 0
                fill_value = graph[i][j] // 5
                for d in range(4):
                    nx, ny = i+dx[d], j+dy[d]
                    if 0<=nx<R and 0<=ny<C and graph[nx][ny] != -1:
                        count += 1
                        new_graph[nx][ny] += fill_value
                new_graph[i][j] += graph[i][j] - count*fill_value
            elif graph[i][j] == -1:
                new_graph[i][j] = -1

    return new_graph
    
def work(graph, aircond):
    x1, x2 = aircond[0], aircond[1] # x좌표
    new_graph = deepcopy(graph)

    # 가로방향 좌표들 옮기기
    new_graph[x1] = [-1, 0] + graph[x1][1:-1] 
    new_graph[x2] = [-1, 0] + graph[x2][1:-1]
    new_graph[0] = graph[0][1:] + [0]
    new_graph[-1] = graph[-1][1:] + [0]

    # 세로방향 좌표들 옮기기
    for i in range(1, R-1):
        if i < x1:
            new_graph[i][0] = graph[i-1][0]
            new_graph[i-1][-1] = graph[i][-1]
        elif i == x1:
            new_graph[i-1][-1] = graph[i][-1]
        elif i > x2:
            new_graph[i][0] = graph[i+1][0]
            new_graph[i+1][-1] = graph[i][-1]
        else:
            new_graph[i+1][-1] = graph[i][-1]
    
    return new_graph
    
R, C, T = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(R)]
aircond = [i for i in range(R) if graph[i][0] == -1]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

for t in range(T):
    after_spread = spread(graph)
    graph = work(after_spread, aircond)

answer = sum(map(sum, graph))
print(answer+2)
