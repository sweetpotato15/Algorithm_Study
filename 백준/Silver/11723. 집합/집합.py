import sys
input = sys.stdin.readline

n = int(input())
S = []
for _ in range(n):
    array = list(input().split())

    if array[0] == "add":
        S.append(int(array[1]))
        S = list(set(S))
    elif array[0] == "remove":
        if int(array[1]) in S:
            S.remove(int(array[1]))
    elif array[0] == "check":
        if int(array[1]) in S:
            print(1)
        else: 
            print(0)

    elif array[0] == "toggle" :
        if int(array[1]) in S:
            S.remove(int(array[1]))
        else:
            S.append(int(array[1]))
    elif array[0] == "all":
        S = list(range(1, 21))
    else:
        S = []