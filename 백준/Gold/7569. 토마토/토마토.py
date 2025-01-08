import sys
input = sys.stdin.readline
import heapq

# 1:익은 토마토, 0:익지않은 토마토, -1: 토마토 없음
# 익은 토마토부터 좌우상하 돌아다니면서 0 -> +1 바꾸기 
M, N, H = map(int, input().split())
tomato = [[] for _ in range(H)]
ripe = [] # [day, H, I, J]

for h in range(H):
    for i in range(N):
        command = list(map(int, input().split()))
        tomato[h].append(command)
        for j in range(M):
            if command[j] == 1:
                ripe.append([1, h, i, j])

while ripe:
    day, h, i, j = heapq.heappop(ripe)
    for dh, di, dj in ((0, -1, 0), (0, 1, 0), (0, 0, -1), (0, 0, 1), (-1, 0, 0), (1, 0, 0)):
        nh, ni, nj = dh+h, di+i, dj+j
        if 0<=nh<H and 0<=nj<M and 0<=ni<N:
            if tomato[nh][ni][nj] == 0:
                heapq.heappush(ripe, [day+1, nh, ni, nj])
                tomato[nh][ni][nj] = day+1

def main():
    max_day = 0
    for h in range(H):
        for i in range(N):
            for j in range(M):
                max_day = max(max_day, tomato[h][i][j])
                if tomato[h][i][j] == 0:
                    return -1
    return max_day-1

print(main())