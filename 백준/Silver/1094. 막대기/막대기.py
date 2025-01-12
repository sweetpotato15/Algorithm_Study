import heapq
X = int(input())
stick = []
heapq.heappush(stick, 64)
while True:
    if sum(stick) <= X:
        print(len(stick))
        break
    elif sum(stick) > X:
        minimum = heapq.heappop(stick)
        if sum(stick)+minimum//2 < X:
            heapq.heappush(stick, minimum//2)
        heapq.heappush(stick, minimum//2)