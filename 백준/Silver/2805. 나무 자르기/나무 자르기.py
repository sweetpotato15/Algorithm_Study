# 0부터 max(height) 를 index로 해서 이진탐색 -> 잘려져서 남은 길이와 필요한 길이를 비교

n, m = map(int, input().split())
height = list(map(int, input().split()))

def TreeHeight(array, start, end, target):
    while start <= end:
        cutter = (start + end) // 2

        # 잘려져서 남은 길이 저장
        remainder = 0
        for i in array:
            if i > cutter:
                remainder += i - cutter

        # 남은 길이가 필요한 길이보다 적다면 절단기 높이 낮추기
        if remainder < target :
            end = cutter - 1
        
        # 남은 길이가 필요한 길이보다 많거나 같으면 일단 절단기 높이 저장하고 최대값 찾기
        else:
            answer = cutter
            start = cutter + 1
    return answer
        
print(TreeHeight(height, 0, max(height), m))