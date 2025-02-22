a, b = map(int, input().split())
graph = [input().strip() for _ in range(a)]
for i in graph:
    print(i[::-1])