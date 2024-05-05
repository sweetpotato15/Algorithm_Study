from itertools import product
import heapq
def num_and_money(users, emoticons, emoticons_discount):
    answer_value = 0
    answer_num = 0
    for i in users:
        d, m = i # 할인율, 서비스 가입 최소금액
        value = 0 # 이모티콘 합 금액
        
        for j in range(len(emoticons)):
            if d <= emoticons_discount[j]:
                value += emoticons[j] * (100 - emoticons_discount[j]) //100
            if value >= m :
                answer_num += 1
                value = 0
                break
        answer_value += value
    return answer_value, answer_num

def solution(users, emoticons):
    # 1. 가입자 최대한 늘리기, 2. 판매액 최대한 늘리기
    # users : [할인율, 서비스 가입 최소금액]
    # 최소 금액이 작은 순으로 
    users = sorted(users, key = lambda x : x[1], reverse = True)
    discount = [40,30,20,10]
    result = []
    emoticons_discount = [] # emoticons 수 만큼 할인율
    # for _ in range(4**len(users)):
    num = len(emoticons)
    myarray = list(product([40,30,20,10], repeat = num))
    for emoticons_discount in myarray:
        a, b = num_and_money(users, emoticons, emoticons_discount)
        heapq.heappush(result, [-b,-a])
        answer = heapq.heappop(result)
        result = [answer]
        
    answer = heapq.heappop(result)
    
    return [-1 * answer[0], -1 * answer[1]]

# 2800 6500 = 9300 * 0.6 = 5580 모두 40% 할인    
# 하나를 30% 로 내리면 