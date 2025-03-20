import sys
input = sys.stdin.readline

N = int(input())
array = list(map(int, input().split()))

smallest = [0]*N
smallest[0] = array[0]

# 연속합
sum_array = array[:]
for i in range(1,N):
    sum_array[i] += sum_array[i-1]
    smallest[i] = min(smallest[i-1], sum_array[i-1])

max_value = max(array)
for i in range(N-1, 0, -1):
    max_value = max(max_value, sum_array[i] - smallest[i], sum_array[i])
print(max_value)