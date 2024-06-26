from collections import defaultdict

# 시간을 입력받으면 sec로 변환
def change_sec(string_time):
    h,m,s = map(int, string_time.split(':'))
    return 3600*h + 60*m + s

def solution(play_time, adv_time, logs): 
    play_time = change_sec(play_time)
    adv_time = change_sec(adv_time)

    # 광고 시작 시간은 logs 의 시작 시간중 하나 
    total_play = [0] * (play_time+1) # total_play[i] : i~i+1초 사이에 존재하는 사람 수
    
    for i in logs:
        total = i.split('-')
        start = change_sec(total[0])
        end = change_sec(total[1])
        
        total_play[start] += 1
        total_play[end] -= 1

    for i in range(1, len(total_play)): 
        total_play[i] += total_play[i-1] 
    for i in range(1, len(total_play)):
        total_play[i] += total_play[i-1] 

    max_count = total_play[adv_time]
    max_start = 0
    for start_time in range(play_time):
        value = start_time + adv_time 
        if value <= play_time:
            end_time = value
        else:
            end_time = play_time

        value = total_play[end_time] - total_play[start_time] 
        if value > max_count:
            max_count = value
            max_start = start_time + 1
    return (f'{max_start//3600:02}:{(max_start%3600)//60:02}:{(max_start%3600)%60:02}')

