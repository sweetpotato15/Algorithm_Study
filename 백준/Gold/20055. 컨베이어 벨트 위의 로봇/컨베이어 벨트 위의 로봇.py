import sys
input = sys.stdin.readline
from collections import deque

n , k = map(int, input().split())
A = list(map(int, input().split()))
#belt = list([i,A[i]] for i in range(2*n)) # (index칸, 각 칸의 내구도)
belt = A # 내구도
robot = [False] * (2*n) # 로봇 위치한 인덱스


# 내구도가 0이면 단계시작
stage = 0
while True :
    stage += 1

    # 과정 1 벨트 회전
    belt.insert(0,belt.pop())
    robot.insert(0,robot.pop())
    if robot[n-1]:
        robot[n-1] = False     

    # 과정 2 전진
    for x in range(n-2,-1,-1): # 맨 앞에 있는 로봇부터
        if robot[x] and not robot[x+1] and belt[x+1] > 0:
            robot[x] = False
            robot[x+1] = True
            belt[x+1] -= 1
    if robot[n-1]:
        robot[n-1] = False

    # 과정 3 로봇 올리기
    if not robot[0] and belt[0] > 0:
        robot[0] = True
        belt[0] -= 1
    
    # 과정 4 내구도 0 개수 확인
    if belt.count(0) >= k:
        print(stage)
        break