import sys
input = sys.stdin.readline

def check_bingo(board, row, col):
    bingo_num = 0
    # 1) 가로줄/세로줄에서 빙고가 나올 경우
    if board[row][5] == 5:
        bingo_num += 1

    if board[5][col] == 5:
        bingo_num += 1    
    
    # 2) 대각선에서 빙고가 나올 경우
    if row == col: # (0, 0), (1, 1), (2, 2), (3, 3), (4, 4)
        if all([visited[i][i] for i in range(5)]):
            bingo_num += 1
    
    if row == 4-col: # (0, 4), (1, 3), (2, 2), (3, 1), (4, 0)
        if all([visited[i][4-i] for i in range(5)]):
            bingo_num += 1
    
    return bingo_num

bingo = [list(map(int, input().split())) + [0] for _ in range(5)] + [[0]*6]
visited = [[False]*5 for _ in range(5)]
command = []
for _ in range(5):
    command += list(map(int, input().split()))

count = 0
for i in range(25):
    if count >= 3:
        print(i)
        break

    number = command[i]
    for row in range(5):
        for col in range(5):
            if bingo[row][col] == number:
                visited[row][col] = True
                bingo[row][5] += 1
                bingo[5][col] += 1

                count += check_bingo(bingo, row, col)
