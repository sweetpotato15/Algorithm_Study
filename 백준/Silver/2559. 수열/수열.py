import sys
input = sys.stdin.readline

n,k = map(int, input().split())
temp = list(map(int, input().split()))

sumvalue = sum(temp[:k])
maximum = sumvalue
for i in range(k,n):
    sumvalue -= temp[i-k]
    sumvalue += temp[i]
    if maximum < sumvalue :
        maximum = sumvalue

print(maximum)