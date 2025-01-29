N = int(input())
array = list(map(int, input().split()))
B, C = map(int, input().split())
answer = 0

array =[max(0,i-B) for i in array]
answer += N

for i in array:
    if i % C ==0:
        answer += i//C
    else:
        answer += i//C+1

print(answer)