# 비슷한 단어 
import sys
input = sys.stdin.readline

n = int(input()) # 총 문자 개수
target = list(input())
answer = 0

for _ in range(n-1):   
    compare = target[:]
    word = input()
    count = 0

    for w in word:
        # 정답 단어와 비교 단어에 공통으로 있는 것 정답에서 제외
        if w in compare:
            compare.remove(w)
        # 정답에 없고 비교에만 있는 문자
        else:
            count += 1
    
    if count < 2 and len(compare) < 2:
        answer += 1

print(answer)