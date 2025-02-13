from collections import deque

N = int(input())
q = deque([(N, 0, [N])]) # (숫자, 횟수, 리스트)
visited = [False]*(N+1)

while q:
    i, cnt, lst = q.popleft()
    visited[i] = True

    if i == 1:
        print(cnt)
        print(*lst)
        break

    if not i%3 and not visited[i//3]: # 3의 배수이면서서 방문하지 않음
        q.append((i//3, cnt+1, lst+[i//3]))
    
    if not i%2 and not visited[i//2]:
        q.append((i//2, cnt+1, lst+[i//2]))
    
    if not visited[i-1]:
        q.append((i-1, cnt+1, lst+[i-1]))
    