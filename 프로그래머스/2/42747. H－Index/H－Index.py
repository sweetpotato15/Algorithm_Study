'''
[[0,6],[1,5],[2,3],[3,1],[4,0]]
[i,j] : j번 이상 인용된 논문이 i+1편 i+1 >= j 가 되어야함

[[0,6],[1,5],[2,3],[3,2],[4,1],[5,0]]
''' 
def solution(citations):
    citations = sorted(citations, reverse=True)
    citations = list(enumerate(citations))
    print(citations)
    if len(citations) == 1:
        if citations[0] == 0:
            return 0
        else:
            return 1
    for a,b in citations:
        if b-a == 1:
            return b
        elif b-a < 1:
            return a
    return len(citations)