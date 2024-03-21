# 배열 A을 오름차순으로 정렬했을 때의 index 값이 원래 배열 순으로 출력되게끔

n = int(input()) # 배열 A의 크기
A = list(map(int, input().split()))
P = [0] * n

sort_A = sorted(A)

# sort 한 값을 하나하나 불러서 index 찾고 값을 0으로 초기화 (중복 값 index 찾기 위해서)

for i in range(n):
    min_index = A.index(sort_A[i])
    P[min_index] = i
    A[A.index(sort_A[i])] = 0

for value in P:
    print(value, end= ' ')