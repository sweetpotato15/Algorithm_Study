import sys
input = sys.stdin.readline

T = int(input())

def LCM(x, y):
    x, y = min(x,y), max(x,y)
    # 최대공약수 구하기
    for i in range(int(x**(1/2)), 1, -1):
        if x % i == 0 and y % i == 0:
            return (x//i) * (y//i) * i
    return x*y

for _ in range(T):
    M, N, x, y = map(int, input().split())
    '''
    M*A+x = N*B+y 되도록 하는 A, B 존재 
    전체 값의 최대값은 M과 N의 최소공배수
    '''
    lcm = LCM(M, N)

    X = [M*i+x for i in range(lcm//M)]
    answer = -1

    for i in X:
        if (i-1)%N+1 == y:
            answer = i
            break
    print(answer)