from collections import deque
def solution(queue1, queue2):

    answer = 0
    q1 = deque(queue1)
    q2 = deque(queue2)
    total = sum(q1) + sum(q2)
    if (sum(queue1) + sum(queue2)) % 2 == 1:
        return -1
    
    target = total//2
    chk = 0
    sum_1 = sum(q1)
    sum_2 = sum(q2)
    
    # sum_1의 경우에 대해서만 생각해주면 됨
    if sum_1 == target:
        return 0
    while q2:
        if sum_1 < target:
            #q1에 대해서만 추가해줌. 루프 탈출을 위해
            now = q2.popleft()
            sum_1 += now
            q1.append(now)
        else:
            now = q1.popleft()
            sum_1 -= now
        answer += 1

        if sum_1 == target:
            chk = 1
            break
            
    if not chk:
        return -1
    return answer