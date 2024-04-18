import sys
input = sys.stdin.readline

n,x = map(int, input().split())
blog = list(map(int, input().split()))

if max(blog) == 0:
    print("SAD")

else:
    count = 1 # 처음 세 값이 최대인 경우 count 해야하기 때문에 1로 초기화
    value = sum(blog[:x])
    maximum = value
    for i in range(x,n):
        value -= blog[i-x]
        value += blog[i]

        if value > maximum:
            maximum = value
            count = 1
        
        elif value == maximum:
            count += 1
    print(maximum)
    print(count)