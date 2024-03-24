n = int(input())
budget_list = list(map(int, input().split()))
budget = int(input())

# ## (def 함수 사용)

def binary_search(array, start, end, target):
    maximum = (start + end) // 2
    remainder = 0
    global answer

    for i in range(n):
        remainder += min(maximum, array[i])

    if start > end:
        answer = maximum
        return answer
    
    if remainder > budget: # 예산 초과인경우
        end = maximum - 1
        binary_search(array, start, end, target)

    else:
        answer = maximum
        start = maximum + 1
        binary_search(array, start, end, target)
    
    return answer


print(binary_search(budget_list, 0, max(budget_list), budget))