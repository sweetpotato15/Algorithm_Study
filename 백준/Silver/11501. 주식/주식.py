import sys
input = sys.stdin.readline
from collections import deque

t = int(input())

def money(day, q):
    answer = 0
    value = q.pop() # 최대값이 될 후보
    while q:
        if value < q[-1]:
            value = q[-1]
            q.pop()
            
        else:# value >= q[-1] 인 경우
            answer += value - q[-1]
            q.pop()
    return answer

        
for _ in range(t):
    n = int(input())
    array = list(map(int, input().split()))
    print(money(n, array))
