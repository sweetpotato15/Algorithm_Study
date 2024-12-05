'''
N행 4열 -> dp 문제
'''
def solution(land):
    graph = [[0]+i+[0] for i in land]+[[0]*6]
    for i in range(1, len(land)+1):
        for j in range(1, 5):
            graph[i][j] = max(graph[i-1][:j]+graph[i-1][j+1:]) + graph[i][j]
    return max(graph[-1])