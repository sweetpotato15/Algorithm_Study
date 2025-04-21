import sys
input = sys.stdin.readline
from collections import deque

N, W, L = map(int, input().split()) # 트럭수, 다리 길이, 다리 최대하중
trucks = deque(list(map(int, input().split())))

bridge = deque([0]*W)
weight = 0
time = 0

for truck in trucks:
    while True:
        ltruck = bridge.popleft()
        weight -= ltruck

        time += 1

        if weight + truck <= L:
            bridge.append(truck)
            weight += truck
            break
        else:
            bridge.append(0)

print(time+W)