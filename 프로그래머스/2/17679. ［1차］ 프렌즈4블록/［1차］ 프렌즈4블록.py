# 같은것 찾기 -> 빈 곳 아래로 채우기 반복
'''
CCBDE CCBDE    DE
AAADE    DE    DE
AAABF    BF CCBBF
CCBBF CCBBF CCBBF
'''

'''
TTTANT
  FA  
   F  
T  RAA
TTMMMF
TMMTTJ
'''
def remove_and_fill(m,n,board):
    global flag

    # 제거할 좌표 담기
    remove_xy = []
    for i in range(m-1):
        for j in range(n-1):
            if board[i][j].isalpha():
                if board[i][j] == board[i][j+1] == board[i+1][j] == board[i+1][j+1]:
                    remove_xy.append([i,j])
    # 제거할 좌표가 없을 경우 flag = True
    if not remove_xy:
        flag = True
        return board
    # 제거하기
    for x,y in remove_xy:
        board[x] = board[x][:y] + '  ' + board[x][y+2:]
        board[x+1] = board[x+1][:y] + '  ' + board[x+1][y+2:]
    # 사라진 부분 채우기
    string = []
    for j in range(n):
        s = ''
        for i in range(m):
            if board[i][j].isalpha():
                s += board[i][j]
        s = s.zfill(m)
        string.append(s)
    board = ['' for _ in range(m)]
    for i in range(n):
        for j in range(m):
            board[j] += string[i][j]
    return remove_and_fill(m,n,board)        
        

def solution(m, n, board):
    answer = remove_and_fill(m,n,board)
    result = 0
    for i in answer:
        result += i.count('0')
    return result