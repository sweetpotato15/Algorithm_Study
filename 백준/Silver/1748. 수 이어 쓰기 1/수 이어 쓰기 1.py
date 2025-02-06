N = input().strip()
digit = len(N) # 몇 자리 수인지

num_array = [0]*(digit+1)
if digit == 1:
    print(N)
else:
    for i in range(1, digit):
        num_array[i] = 9*10**(i-1)
    num_array[digit] = int(N) - sum(num_array)
    answer = sum([i*num_array[i] for i in range(digit+1)])
    print(answer)