import sys
input = sys.stdin.readline
sys.setrecursionlimit(int(1e6))
N, r, c = map(int, input().split())

def dfs(start, r, c, n):
    if n==1:
        if r==0:
            print(start+c)
            return 
        else:
            print(start+1+c+r)
            return 

    num = 2**(2*n-2) # 다음 단계 사각형 개수 
    line = 2**(n-1) # 다음 단계 한 변의 길이
    if 0<=r<line:
        if 0<=c<line: # 좌측 위에 위치
            dfs(start+num*0, r, c, n-1)
        else: # 우측 위에 위치
            dfs(start+num, r, c-line, n-1)

    else:
        if 0<=c<line: # 좌측 아래에 위치
            dfs(start+num*2, r-line, c, n-1)
        else: # 우측 아래에 위치
            dfs(start+num*3, r-line, c-line, n-1)

dfs(0, r, c, N)
