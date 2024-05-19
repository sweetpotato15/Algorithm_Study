def solution(id_list, report, k):
    n = len(id_list)
    answer = [0] * n

    id_dict = {x : 0 for x in id_list}

    for i in set(report):
        id_dict[i.split()[1]] += 1
    
    for i in set(report):
        if id_dict[i.split()[1]] >= k:
            answer[id_list.index(i.split()[0])] += 1
    
    return answer
   