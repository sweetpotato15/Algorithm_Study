import sys
input = sys.stdin.readline
n = int(input())
meeting = [list(map(int, input().split())) for _ in range(n)]

meeting = sorted(meeting, key = lambda x : (x[1],x[0]))
end_time = meeting[0][1]
count =1
for i in range(1, n):
    if meeting[i][0] >= end_time:
        count += 1
        end_time = meeting[i][1]
print(count)