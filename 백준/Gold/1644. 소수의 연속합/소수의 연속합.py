# 소수의 연속합 1644
import sys
input = sys.stdin.readline

# 에라토스테네스의 체 
def prime_list(n):
    sieve = [True] * (N+1)
    for i in range(2, int(n**(1/2))+1):
        if sieve[i] == True: # i가 소수인 경우 
            for j in range(i+i, n+1, i):
                sieve[j] = False
    return [i for i in range(2, n+1) if sieve[i]]

N = int(input())

if N == 1:
    print(0)
else:
    number = prime_list(N)

    count = 0
    start = 0
    end = 0
    value = number[start]
    while start <= end < len(number):
        if value == N:
            count += 1
            value -= number[start]
            start += 1
        elif value < N and end < len(number)-1:
            end += 1
            value += number[end]
        else:
            value -= number[start]
            start += 1
    print(count)