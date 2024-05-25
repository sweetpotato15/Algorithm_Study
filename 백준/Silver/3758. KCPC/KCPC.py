import sys
input = sys.stdin.readline

def kcpc(n,k,id,m):
    # 0 : 제출 횟수, 나머지는 문제에 대한 점수
    score = [{x : 0 for x in range(1, k+1)} for _ in range(n) ]
    submit = [0] * n
    team = []
    for i in range(m):
        a,b,c = map(int, input().split())
        score[a-1][b] = max(score[a-1][b],c)
        submit[a-1] += 1
        team.append(a-1)
    team = team[::-1]
    # 점수, 제출 횟수, 마지막으로 제출 시간 , 팀 id-1
    sum_score = [[sum(score[i].values()), submit[i], team.index(i),i] for i in range(n)]
    sum_score = sorted(sum_score, reverse =True, key = lambda x : (x[0],-x[1],x[2]))

    for i in range(n):
        if sum_score[i][3] == id-1:
            return i+1

t = int(input())
for _ in range(t):
    n,k,id,m = map(int, input().split())
    print(kcpc(n,k,id,m))
