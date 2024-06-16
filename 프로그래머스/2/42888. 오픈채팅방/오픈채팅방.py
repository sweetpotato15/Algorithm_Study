# 0606
# change 면 해당 아이디 닉네임 변경
def solution(record):
    record = [x.split() for x in record]
    name_dict = {}
    answer = []
    for i in range(len(record)):
        if record[i][0] == 'Enter':
            name_dict[record[i][1]] = record[i][2]
        elif record[i][0] == 'Change':
            name_dict[record[i][1]] = record[i][2]
    for i in record:
        if i[0] == 'Enter':
            answer.append(f'{name_dict[i[1]]}님이 들어왔습니다.')
        elif i[0] == 'Leave':
            answer.append(f'{name_dict[i[1]]}님이 나갔습니다.')
    return answer
            

    
