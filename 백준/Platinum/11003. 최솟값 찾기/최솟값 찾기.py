import sys
from collections import deque
input = sys.stdin.readline

N, L = map(int, input().split())
now = list(map(int, input().split()))
mydeque = deque()

for i in range(N):
    while mydeque and mydeque[-1][0] > now[i]:
        mydeque.pop()
    mydeque.append((now[i],i))
    if mydeque[0][1] <= i-L : 
        mydeque.popleft()
    print(mydeque[0][0], end=" ")
        
        