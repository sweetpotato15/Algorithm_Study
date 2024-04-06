# 진실을 아는 사람과 같이 만나는 다른 사람들에게도 진실 
# union 진실을 아는 사람, 그 사람 제외한 같은 모임 다른 사람
import sys
from collections import deque
input = sys.stdin.readline

n , m = map(int, input().split()) # n 사람의 수 m 파티의 수
true = list(map(int, input().split()))
party = [ list(map(int, input().split())) for _ in range(m)]

# 진실을 아는 사람이 없을 떄
if true[0] == 0:
    print(m)

# 진실을 아는 사람이 있을 때
else:
    answer = [1] * (m) # 진실말해야하면 0, 거짓말 해야하면 1
    q = deque(true[1:])
    while q:
        true_person = q.popleft()
        for i in range(m):            
            if true_person in party[i][1:]:
                q += deque(party[i][1:])
                party[i] = []
                answer[i] = 0
    print(sum(answer))