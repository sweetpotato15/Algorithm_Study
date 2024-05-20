n = int(input())
array = [list(map(int, input().split())) for _ in range(n)]
array = sorted(array, key = lambda x : x[0])

maximum = sorted(array, reverse = True, key = lambda x : x[1])[0]
maximum_index = array.index(maximum)
answer = maximum[1]

x, y = array[0]
for i in range(maximum_index+1):
    if array[i][1] >= y : # 이전 y값보다 더 크다면 더해주기
        height = y
        width = array[i][0] - x
        answer += height * width
        x, y = array[i]

x, y = array[-1]
for i in range(n-1, maximum_index-1, -1):
    if array[i][1] >= y:
        height = y
        width = x - array[i][0]
        answer += height * width
        x, y = array[i]

print(answer)