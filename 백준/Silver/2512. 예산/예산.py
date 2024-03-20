n = int(input())
budget = list(map(int, input().split()))
maximum = int(input())


# 0, max(budget)을 index 로 잡고 이진탐색 
# maximum 값과 합친 금액을 비교

def Budget(array, start, end, target):
    while start <= end:
        my_max = (start + end) // 2

        money = 0
        for i in array:
            money += min(my_max, i)

        # 총 예산이 더 적을 경우에는 상한액 내리기
        if money > target :
            end = my_max - 1
        
        # 총 예산이 많거나 같을 경우에는 일단 저장 후 상한액 올리기
        else:
            answer = my_max
            start = my_max + 1

    return answer

print(Budget(budget, 0, max(budget), maximum))