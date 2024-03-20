x, y = map(int, input().split())

# 0 부터 x까지를 index 로 잡고 이진탐색 
# 원래 승률과 차이가 1이상 날때까지

def Win(start,end,x,y):
    if (y * 100 ) //x >= 99 :
        return -1
    else:
        while start <= end:
            original = (y * 100 ) //x
            mid = (start + end) // 2

            new = ((y+mid) * 100 ) // (x+mid) 

            if new - original < 1:
                start = mid + 1

            else: 
                answer = mid
                end = mid - 1
        return answer
    
print(Win(0, x, x, y))
        