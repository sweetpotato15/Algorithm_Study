import sys
input = sys.stdin.readline
from collections import deque
card = deque(list(range(1,int(input())+1)))
while card:
    if len(card) == 1:
        print(*card)
        break 
    card.popleft()
    card.append(card.popleft())