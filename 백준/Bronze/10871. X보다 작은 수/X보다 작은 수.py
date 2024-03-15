n,x  = map(int, input().split())
arr1 = list(map(int, input().split()))

for i in arr1:
    if i < x:
        print(i,end=' ')