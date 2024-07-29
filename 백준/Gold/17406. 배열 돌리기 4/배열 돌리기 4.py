import sys
input = sys.stdin.readline
from collections import deque
from itertools import permutations
from copy import deepcopy

def rotate_array(array,rotate_info):
    r,c,s = rotate_info # s 횟수만큼 반복
    for i in range(1, s+1): # 시작지점 (r-i, c-i)
        start_x, start_y = r-i, c-i

        ori = deque()
        # rotate 돌리는 한 변 길이가 2*i
        # 위 가로, 오른쪽 세로, 아래 가로, 왼쪽 세로
        for dy in range(2*i):
            ori.append(array[start_x][start_y+dy])
        for dx in range(2*i):
            ori.append(array[start_x+dx][start_y+2*i])
        for dy in range(2*i,0,-1):
            ori.append(array[start_x+2*i][start_y+dy])
        for dx in range(2*i,0,-1):
            ori.append(array[start_x+dx][start_y])
        
        ori.rotate(1)
        
        for dy in range(2*i):
            array[start_x][start_y+dy] = ori.popleft()
        for dx in range(2*i):
            array[start_x+dx][start_y+2*i] = ori.popleft()
        for dy in range(2*i,0,-1):
            array[start_x+2*i][start_y+dy] = ori.popleft()
        for dx in range(2*i,0,-1):
            array[start_x+dx][start_y] = ori.popleft()

    return array

def find_minimum(array):
    value = int(1e5)
    for i in array[1:-1]:
        value = min(value, sum(i))
    return value
        
N, M ,K = map(int, input().split())
array_ori = [[0]*(M+2)] + [[0]+list(map(int, input().split()))+[0] for _ in range(N)] + [[0]*(M+2)]
rotate_info = [list(map(int, input().split())) for _ in range(K)]
minimum = int(1e5)

for order in list(permutations(range(K),K)):
    array = deepcopy(array_ori)
    for o in order:
        array = rotate_array(array, rotate_info[o])
    minimum = min(minimum, find_minimum(array))

print(minimum)