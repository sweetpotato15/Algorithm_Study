t = int(input())

def tree_level(n, array):
    array.sort()
    answer = [0] * n
    for i in range(0,n//2): 
        answer[i] = array[2*i]
        answer[-(i+1)] = array[2*i+1]
    if n % 2 == 1:
        answer[n//2] = array[-1]
    
    diff = [abs(answer[i] - answer[i-1]) for i in range(1,n)]
    return max(max(diff), answer[-1] - answer[0])

for i in range(t):
    n = int(input())
    array = list(map(int, input().split()))
    print(tree_level(n, array), end = ' ')