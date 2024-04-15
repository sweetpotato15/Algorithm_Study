import sys
from bisect import bisect_right
from collections import deque
input = sys.stdin.readline

t = int(input())

def Line():
    array = list(map(int, input().split()))
    x = array[0]
    array = array[1:]
    array = deque(array)
    count = 0
    answer = []
    for i in range(len(array)):
        now = array.popleft()
        index = bisect_right(answer, now)
        answer.insert(index, now)
        if index != len(answer)-1:
            count += len(answer) -1 - index 
        answer.sort()
    print(x,count)

for _ in range(t):
    Line()
