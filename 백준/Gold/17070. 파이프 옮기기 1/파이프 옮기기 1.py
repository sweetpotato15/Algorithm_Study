import sys
input = sys.stdin.readline

N = int(input())
house = [[1]*(N+2)] + [[1]+list(map(int,input().split()))+[1] for _ in range(N)] + [[1]*(N+2)]
count = 0

# dir -  가로 (0), 세로 (1), 대각선 (2), pipe1의 정보는 필요없으므로 pipe2의 좌표만 입력
def dfs(x,y, dir):
    global count

    if x == N and y == N:
        count += 1
        return 
    
    # pipe2를 기준으로 total 리스트에 [오른쪽, 아래, 대각선] 순으로 house 값 입력
    total = [house[x][y+1], house[x+1][y], house[x+1][y+1]]
    if (dir == 1 or dir == 2) and total[1] == 0 : # (현재 세로 or 대각선) -> (다음 세로)
        dfs(x+1,y,1)
    
    if (dir == 0 or dir == 2) and total[0] == 0 : # (현재 가로 or 대각선) -> (다음 가로)
        dfs(x,y+1,0)
    
    if sum(total) == 0:
        dfs(x+1,y+1,2)

if house[N][N] == 1 or (house[1][3]==1 and house[2][2]==1) or (house[N][N-1]==1 and house[N-1][N] ==1):
    print(0)
    exit()

dfs(1,2,0)
print(count)