N = int(input())
array = sorted(list(map(int, input().split())))
answer = array[0]*array[-1]
print(answer)