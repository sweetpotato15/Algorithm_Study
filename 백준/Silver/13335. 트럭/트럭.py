import sys
input = sys.stdin.readline
from collections import deque

N, W, L = map(int, input().split()) # 트럭수, 다리 길이, 다리 최대하중
array = deque(list(map(int, input().split())))

ans = 0
q = deque([0]*W, maxlen=W)
while array or q:
    if q[0]: 
        q.popleft()

    if array and sum(q) + array[0] <= L:
        q.append(array.popleft())

    else:
        q.append(0)

    ans += 1

    if sum(q) == 0:
        break
print(ans)
