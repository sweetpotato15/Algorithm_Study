import sys
input = sys.stdin.readline

n, k = map(int, input().split()) # 총 n개 국가, k등이 누구인지
medal = [ list(map(int, input().split())) for _ in range(n) ]

medal = sorted(medal, key = lambda x : (x[1],x[2],x[3]) , reverse = True)

for i in range(n-1):
    if medal[i][1:] == medal[i+1][1:]:
        medal[i].append(i+1)
        medal[i+1].append(medal[i][4])
    else:
        medal[i].append(i+1)

for i in range(n):
    if medal[i][0] == k:
        print(medal[i][4])