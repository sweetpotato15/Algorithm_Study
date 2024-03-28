row, col= map(int, input().split())

my_board = [[0] for _ in range(row)]
for i in range(row):
    my_board[i] = input()

chess = ['W','B']

white = ["" for _ in range(row)]
black = ["" for _ in range(row)]

for i in range(row):
    for j in range(col):
        white[i] += chess[(i+j)%2]
        black[i] += chess[(i+j)%2-1]

white_answer = [[0]*(col) for _ in range(row)]
black_answer = [[0]*(col) for _ in range(row)]

for i in range(row):
    for j in range(col):
        if my_board[i][j] != white[i][j]:
            white_answer[i][j] = 1
        else:
            black_answer[i][j] = 1

answer = []

for i in range(0,row-8+1):
    for j in range(0, col-8+1):
        count = 0
        for x in range(8):
            for y in range(8):
                count += white_answer[x+i][y+j]
        answer.append(count)
        answer.append(64-count)

print(min(answer))