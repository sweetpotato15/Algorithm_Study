import sys
input = sys.stdin.readline

N, M, x, y, K = map(int, input().split()) # x, y : 현재 바닥면이 위치한 좌표 
graph = [list(map(int, input().split())) for _ in range(N)]
dice = [0, 0, 0, 0, 0, 0] # dice[5] : 바닥 / dice[0] : 위

command = list(map(int, input().split()))

dice_map = {1 : [4, 2, 1, 6, 5, 3],
            2 : [3, 2, 6, 1, 5, 4],
            3 : [5, 1, 3, 4, 6, 2],
            4 : [2, 6, 3, 4, 1, 5]}
dice_pos = {1 : [0, 1],
            2 : [0, -1],
            3 : [-1, 0],
            4 : [1, 0]}

for c in command:
    nx, ny = x+dice_pos[c][0], y+dice_pos[c][1]

    # 지도 바깥으로 이동하는 경우 
    if not (0<=nx<N and 0<=ny<M): 
        continue

    dice = [dice[i-1] for i in dice_map[c]]
    x, y = nx, ny
    if graph[x][y] == 0: # 이동한 칸에 쓰여있는 수가 0
        graph[x][y] = dice[5]
    else: # 이동한 칸에 쓰여있는 수가 0이 아닌 경우
        dice[5] = graph[x][y]
        graph[x][y] = 0
    print(dice[0])

