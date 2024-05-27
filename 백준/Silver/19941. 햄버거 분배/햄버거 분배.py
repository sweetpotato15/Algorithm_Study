import sys
input = sys.stdin.readline
from collections import deque

n, k = map(int, input().split())
string = input().strip()

hamburger, person = deque(), deque()

for i in range(n):
    if string[i] == 'H': hamburger.append(i)
    else: person.append(i)

count = 0
while person and hamburger:
    h = hamburger.popleft()
    p = person.popleft()
    if h-k <= p <= h+k:
        count += 1

    # 사람이 더 클 경우 다시 append
    elif p > k+h:
        person.appendleft(p)
    else:
        hamburger.appendleft(h)

print(count)