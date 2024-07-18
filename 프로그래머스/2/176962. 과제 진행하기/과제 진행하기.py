'''
https://school.programmers.co.kr/learn/courses/30/lessons/176962
'''
'''
[과목명, 시작시간, 소요시간]


'''
def time_to_min(string):
    h, m = map(int,string.split(':'))
    return 60*h+m

def solution(plans):
    plans = sorted(plans, key = lambda x : x[1])
    schedule = []
    for i in range(len(plans)):
        schedule.append([plans[i][0], time_to_min(plans[i][1]), int(plans[i][2])])
    
    conti = [] # stack 선입후출, [과목명, 남은시간]
    complete = []
    
    for i in range(len(plans)-1):
        now = schedule[i] # [과목명, 시작시간, 소요시간]
        nex = schedule[i+1]
        
        left = nex[1] - (now[1]+now[2])
        if left >= 0:
            complete.append(schedule[i][0])            
            while conti and left > 0:
                add = conti.pop()
                left -= add[1]
                if left >= 0:                
                    complete.append(add[0])
                else:
                    conti.append([add[0], abs(left)])
        else:
            conti.append([schedule[i][0], abs(left)]) 
    
    complete.append(schedule[-1][0])
    for i in conti[::-1]:
        complete.append(i[0])
        
    return complete