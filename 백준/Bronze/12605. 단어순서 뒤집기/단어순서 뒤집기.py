N = int(input())
for i in range(N):
    string = input().split()
    print(f'Case #{i+1}: {' '.join(string[::-1])}')