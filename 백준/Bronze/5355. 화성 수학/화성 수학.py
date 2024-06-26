T = int(input())
for _ in range(T):
    array = list(input().split())
    num = float(array.pop(0))
    while array:
        now = array.pop(0)
        if now == '@':
            num *= 3
        elif now == '#':
            num -= 7
        elif now == '%':
            num += 5

    print(f'{num:.2f}')