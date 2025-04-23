import sys
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    N = int(input())
    score = sorted([[i] + list(map(int, input().split())) for i in range(N)], key=lambda x:(x[1], x[2]))
    array = [True]*N

    min_interview = score[0][2]
    for i, document, interview in score[1:]:
        if interview > min_interview:
            array[i] = False
            continue
        min_interview = min(interview, min_interview)


    print(sum(array))