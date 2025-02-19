import sys
from itertools import combinations
input = sys.stdin.readline

height = [int(input()) for _ in range(9)]
answer = []

index = list(combinations(range(9), 7))
for i in index:
    sum_value = 0
    for j in i:
        sum_value += height[j]
    if sum_value == 100:
        answer = [height[j] for j in i]
for i in sorted(answer):
    print(i)