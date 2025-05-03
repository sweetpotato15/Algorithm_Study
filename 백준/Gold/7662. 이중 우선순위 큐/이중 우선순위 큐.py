import sys
input = sys.stdin.readline
import heapq

def isEmpty(items):
    for item in items:
        if item[1] > 0:
            return False
    return True

T = int(input())
for _ in range(T):
    k = int(input())
    max_heap = []
    min_heap = []
    dict = {}
    for _ in range(k):
        command, num = input().split()
        num = int(num)

        if command == 'I':
            if num in dict:
                dict[num] += 1
            else:
                dict[num] = 1
            heapq.heappush(max_heap, -num)
            heapq.heappush(min_heap, num)
        
        else:
            if not isEmpty(dict.items()):
                if num == -1: # 최소값 제거
                    while min_heap[0] not in dict or dict[min_heap[0]] < 1:
                        temp = heapq.heappop(min_heap)
                        if temp in dict:
                            del(dict[temp])
                    dict[min_heap[0]] -= 1
                else: # 최대값 제거
                    while -max_heap[0] not in dict or dict[-max_heap[0]] < 1:
                        temp = -heapq.heappop(max_heap)
                        if temp in dict:
                            del(dict[temp])
                    dict[-max_heap[0]] -= 1

    if isEmpty(dict.items()):
        print('EMPTY')
    else:
        while min_heap[0] not in dict or dict[min_heap[0]] < 1:
            heapq.heappop(min_heap)
        while -max_heap[0] not in dict or dict[-max_heap[0]] < 1:
            heapq.heappop(max_heap)
        print(-max_heap[0], min_heap[0])


            