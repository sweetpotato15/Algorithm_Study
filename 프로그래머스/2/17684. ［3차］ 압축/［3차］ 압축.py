def solution(msg):
    my_dict = {}
    for i in range(65, 91):
        my_dict[chr(i)] = i-64
    answer = []
    new_index = 27
    
    # # 현재 입력에 대한 출력 추가 -> 다음 글자 합쳐서 사전에 등록
    now = ''
    for s in msg:
        now += s
        if now in my_dict.keys():
            continue
        else:
            my_dict[now] = new_index
            new_index += 1
            answer.append(my_dict[now[:-1]])
            now = now[-1]
    answer.append(my_dict[now])        
    return answer
