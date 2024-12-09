def solution(n, left, right):
    x1, y1 = left//n, left%n
    x2, y2 = right//n, right%n
    answer = []
    for i in range(x1, x2+1): # i행 시작 하는 숫자 : i+1
        row = [i+1 for _ in range(i+1)] + list(range(i+2,n+1))
        if x1 == x2:
            answer = row[y1:y2+1]
            return answer
        if i == x1:
            answer += row[y1:]
        elif i == x2:
            answer += row[:y2+1]
        else:
            answer += row
    return answer



