M = int(input())
N = int(input())

answer1 = [i**2 for i in range(int(M**(1/2)), int(N**(1/2))+1) if M<=i**2<=N]
if answer1:
    print(sum(answer1))
    print(answer1[0])
else:
    print(-1)