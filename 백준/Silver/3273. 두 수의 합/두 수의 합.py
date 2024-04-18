import sys
input = sys.stdin.readline

n = int(input())
number = list(map(int, input().split()))
target = int(input())
number.sort()

start = 0
end = n-1
count = 0
while start < end:
    if number[start] + number[end] == target :
        count += 1
        start += 1
        end -= 1
    elif number[start] + number[end] < target :
        start += 1
    else:
        end -= 1
print(count)