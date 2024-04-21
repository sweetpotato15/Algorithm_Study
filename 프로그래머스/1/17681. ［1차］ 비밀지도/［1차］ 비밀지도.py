  
def solution(n, arr1, arr2):
    answer1 = [[] for _ in range(n)]
    answer2 = [[] for _ in range(n)]
    for j in range(n):
        num1 = arr1[j]
        num2 = arr2[j]
        for i in range(n-1, -1, -1):
            answer1[j].append(num1 // (2**i))
            num1 = num1 % (2**i)
            answer2[j].append(num2 // (2**i))
            num2 = num2 % (2**i)    
    answer = [[0]*n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if answer1[i][j] == 0 and answer2[i][j] == 0:
                answer[i][j] = "0"
            else:
                answer[i][j] = "1"
    result = [""] * n
    for i in range(n):
        for j in range(n):
            result[i] += answer[i][j]
    real = [""] * n
    for i in range(n):
        for j in range(n):
            if result[i][j] == "1":
                real[i] += "#"
            else:
                real[i] += " "
    return real