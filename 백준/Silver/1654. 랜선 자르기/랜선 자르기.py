n, target = map(int, input().split())
height = []
for _ in range(n):
    height.append(int(input()))


# 0부터 max(height)까지를 index로 해서 이진탐색
# cutter로 나눈 몫을 저장해서 필요한 랜선 개수랑 비교

def LAN(height, start, end, target):
    while start <= end:
        cutter = (start + end) // 2

        # cutter로 잘랐을 때 몇개 나오는지 저장
        remainder = 0
        for i in height:
            if i != 0:
                remainder += i // cutter
        
        # 잘라진 개수가 필요한 개수보다 적다면 cutter 길이 줄이기
        if remainder < target:
            end = cutter - 1
        
        # 잘라진 개수가 필요한 개수보다 많다면 cutter 길이 저장 후 늘리기
        else:
            answer = cutter
            start = cutter + 1
    
    return answer

print(LAN(height, 1, max(height), target))