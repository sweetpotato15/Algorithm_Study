import sys
input = sys.stdin.readline

n,m,inventory = map(int, input().split())
block = []
for i in range(n):
    array = list(map(int, input().split()))
    block += array
block.sort()

def mytime(array, height, inventory):
    time = 0
    b = inventory
    for i in range(len(array)):
        if array[i] >= height:
            time += 2 * (array[i] - height)
            b += array[i] - height
        else:
            time += height - array[i]
            b -= height - array[i]
    if b < 0:
        time = 500 * 500 * max(array) * 2
    
    return time

answer = []
for i in range(min(block), max(block)+1):
    a = mytime(block, i, inventory)
    answer.append((a,i))
    if a > 1e9:
        break

answer.sort(key = lambda x : (x[0], -x[1]))

print(*answer[0])
