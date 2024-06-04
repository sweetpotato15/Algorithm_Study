import sys
input = sys.stdin.readline

n = int(input())
# graph = [[] for _ in range(n+1)]

# for i in range(1, n+1):
#     node = int(input())
#     graph[node].append(i) # i -> node 간선
# print(graph)

# for i in range(1, n+1): 
#     if not graph[i]:

graph = {i:[] for i in range(1, n+1)}
for i in range(1,n+1):
    node = int(input())
    graph[node].append(i)

while True:
    empty = [i for i in graph.keys() if not graph[i]]
    if not empty:
        break
    for j in empty:
        for i in graph.keys():
            if j in graph[i]:
                del graph[i][graph[i].index(j)]
        del graph[j]

answer = graph.values()
print(len(answer))
for i in sorted(answer):
    print(*i)
