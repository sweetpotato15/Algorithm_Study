# 자카드 유사도 : 교집합 크기 / 합집합 크기 (둘다 공집합일 경우에는 1)


def solution(str1, str2):
    str1 = str1.strip().lower()
    str2 = str2.strip().lower()
    A, B = [], []
    for i in range(len(str1)-1):
        if str1[i].isalpha() and str1[i+1].isalpha():
            A.append(str1[i:i+2])
    for i in range(len(str2)-1):
        if str2[i].isalpha() and str2[i+1].isalpha():
            B.append(str2[i:i+2])
            
    A1 = list(set(A))
    B1 = list(set(B))
    
    up = 0
    for i in A1:
        if i in B:
            up += min(A.count(i),B.count(i))
            
    down = len(A) + len(B) - up

    if down == 0:
        return 65536
    else:
        return int((up/down)*65536)

