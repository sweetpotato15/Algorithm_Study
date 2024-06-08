import sys
input = sys.stdin.readline

n = int(input())
array = list(map(int, input().split()))

memory = [0] * 100001
start , end = 0, 0
count = 0
while end < n:
    if not memory[array[end]]:
        memory[array[end]] += 1
        end += 1
    else:
        count += end - start
        memory[array[start]] -= 1
        start += 1

count += ((end-start)*(end-start+1)) // 2
print(count)
