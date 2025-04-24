import sys
input = sys.stdin.readline

graph = [[False]*100 for _ in range(100)]
for _ in range(4):
    x1, y1, x2, y2 = map(int, input().split())
    x1, y1, x2, y2 = x1, 100-y1, x2, 100-y2
    for i in range(x1, x2):
        for j in range(y2, y1):
            graph[i][j] = True

print(sum(map(sum, graph)))