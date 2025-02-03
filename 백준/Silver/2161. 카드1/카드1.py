N = int(input())

from collections import deque

array = list(range(1, N+1))
array = deque(array)

while True:
    if not array:
        break
    num = array.popleft()
    print(num, end=' ')
    array.rotate(-1)