import sys
input = sys.stdin.readline

def check_lst(lst):
    visited = [False]*N
    if len(set(lst)) == 1:
        return True
    for i in range(1, N):
        if abs(lst[i] - lst[i-1]) > 1: # 경사로 못 놓는 경우
            return False
        elif lst[i] - lst[i-1] == 1: # 왼쪽으로 다리 놓는 경우
            if i < L: # 왼쪽에 공간이 없는 경우 
                return False
            for j in range(L):
                if lst[i-1] != lst[i-1-j] or visited[i-1-j]:
                    return False
                visited[i-1-j] = True
        elif lst[i] - lst[i-1] == -1: # 오른쪽으로 다리 놓는 경우 
            if N-i < L: # 오른쪽에 공간이 없는 경우
                return False 
            for j in range(L):
                if lst[i] != lst[i+j] or visited[i+j]:
                    return False
                visited[i+j] = True
    return True

N, L = map(int, input().split()) # 지도 크기, 경사로 길이 
graph = [list(map(int, input().split())) for _  in range(N)]

answer = 0
for i in graph:
    answer += check_lst(i)
for i in zip(*graph):
    answer += check_lst(i)
print(answer)