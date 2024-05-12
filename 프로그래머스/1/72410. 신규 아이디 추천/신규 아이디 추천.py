def solution(new_id):
    my_id = ''
    word = ['-','_','.']

    for i in range(len(new_id)):
        # 1. 소문자 치환
        if new_id[i].isalpha():
            my_id += new_id[i].lower()

        # 2. 문자 숫자 이외 제거    
        elif new_id[i].isdigit():
            my_id += new_id[i]
            
        elif new_id[i] in word:
            my_id += new_id[i]

    #3. ... 연속 
    dot = 0
    answer = ''
    for i in range(len(my_id)):
        if my_id[i] != ".":
            answer += my_id[i]
            dot = 0
        else:
            dot += 1
            if dot == 1: answer += "."

    # 4. 앞뒤 제거
    if answer and answer[0] == "." : answer = answer[1:]
    if answer and answer[-1] == "." : answer = answer[:-1]

    # 5. 빈 문자열
    if not answer: answer = "a"
    
    # 6. 
    if len(answer) >= 16: answer = answer[:15]
    if answer[-1] == "." : answer = answer[:-1]

    # 7. 
    if len(answer) == 1:
        answer += answer[0] + answer[0]
    elif len(answer) == 2:
        answer += answer[-1]



    return answer