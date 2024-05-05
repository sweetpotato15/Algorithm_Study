def solution(survey, choices):
    #rt, cf, jm, an
    type = ['R','T','C','F','J','M','A','N']
    type_dict = {}
    for i in type:
        type_dict[i] = 0
        
    for i in range(len(survey)):
        word = survey[i]
        if choices[i] == 4:
            continue
        elif choices[i] < 4:
            type_dict[word[0]] += 4 - choices[i]
        else:
            type_dict[word[1]] += choices[i] - 4
    answer = ''
    value_list = list(type_dict.values())
    key_list = list(type_dict.keys())
    for i in range(0,8,2):
        if value_list[i] > value_list[i+1]:
            answer += key_list[i]
        elif value_list[i] < value_list[i+1]:
            answer += key_list[i+1]
        else:
            answer += sorted([key_list[i], key_list[i+1]])[0]
    return answer
