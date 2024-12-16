import sys
input = sys.stdin.readline

def solution():
    N = int(input())
    fassion = {}
    for _ in range(N):
        a, b = input().split()
        if b in fassion.keys():
            fassion[b] += [a]
        else:
            fassion[b] = [a]
    ans = [len(x)+1 for x in fassion.values()]
    result = 1
    for i in ans:
        result *= i
    print(result-1)

'''
상의 - 3가지
하의 - 2가지
얼굴 - 5가지
안입는거 - x

3+2+5 + 3*2 + 3*5+ 2*5 + 2*3*5
[3, 2, 5]
a+b+c+ab+bc+ca+abc = (1+a)(1+b)(1+c)-1
'''
T = int(input())
for _ in range(T):
    solution()

