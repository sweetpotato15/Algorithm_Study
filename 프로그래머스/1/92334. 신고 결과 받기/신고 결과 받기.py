def solution(id_list, report, k):
    n = len(id_list)
    # 각 아이디를 index로 변환
    id_index = {} # id : index 형태
    for i in range(n):
        id_index[id_list[i]] = i
    
    M = [[0] * n for _ in range(n)]

    for i in range(len(report)):
        a, b = report[i].split()
        a = id_index[a]
        b = id_index[b]
        M[a][b] = 1 # a가 b를 신고
    
    # 내가 누구를 신고했는지 -> 행, 누가 나를 신고했는지 -> 열

    stop_index = [] # 정지된 유저 index
    for i in range(n):
        count = 0
        for j in range(n):
            count += M[j][i]
            if count == k:
                stop_index.append(i)
                break

    report_index = [] # 정지된 유저를 누가 신고했는지
    for i in range(n):
        count = 0
        for index in stop_index:
            if M[i][index] == 1:
                count += 1
        report_index.append(count)
    answer = report_index
    return answer