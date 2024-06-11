n = int(input())
count = [int(input()) for _ in range(n)]
if sum(count) > n - sum(count): # 1 > 0
    print('Junhee is cute!')
else:
    print('Junhee is not cute!')