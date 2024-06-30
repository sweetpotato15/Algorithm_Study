import sys
input = sys.stdin.readline

N = int(input())
akbo = [0] + list(map(int, input().split()))
Q = int(input())

answer = [0] * (N+1) # i난이도 > i+1난이도 이면 i번 실수 , i번이 마지막 곡이라면 실수 아님
for i in range(1,N):
    plus = 0
    if akbo[i] > akbo[i+1]:
        plus = 1
    answer[i] = answer[i-1] + plus

for _ in range(Q):
    x, y = map(int, input().split())
    print(answer[y-1] - answer[x-1])