import sys
input = sys.stdin.readline

n = int(input())

start = 1
end = 2

count = 1
value = start + end
while start < end:
    if value == n:
        count += 1
        value -= start
        start += 1
    elif value < n:
        end += 1
        value += end
    else:
        value -= start
        start += 1
        
if n <= 2:
    print(1)
else:
    print(count)