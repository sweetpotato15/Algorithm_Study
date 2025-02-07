N = int(input())

array = list(range(1, 4))

for _ in range(N):
    a, b = map(int, input().split())
    a_i = array.index(a)
    b_i = array.index(b)

    array[a_i], array[b_i] = b, a
print(array[0])