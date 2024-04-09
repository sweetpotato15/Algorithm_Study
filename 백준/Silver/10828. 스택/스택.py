import sys
input = sys.stdin.readline


n = int(input())
answer = []
for _ in range(n):
    command = list(input().split())
    if command[0] == "push":
        answer.append(int(command[1]))
    elif command[0] == "top":
        if not answer:
            print(-1)
        else: print(answer[-1])
    elif command[0] == "size":
        print(len(answer))
    elif command[0] == "empty":
        if not answer:
            print(1)
        else: print(0)
    else:
        if not answer:
            print(-1)
        else: print(answer.pop())