import sys
input = sys.stdin.readline
from bisect import bisect_left, bisect_right

n, new, p = map(int, input().split())
if n > 0:
    score = list(map(int, input().split()))

if n == 0 :
    answer = 1
else:
    # 새로운 값이 리스트 내에 있는 가장 작은 수보다 같거나 작을 경우 
    if score[-1] >= new and len(score) >= p:
        answer = -1
    else:
        score = sorted(score)
        answer = len(score) + 1 - bisect_right(score, new)
print(answer)