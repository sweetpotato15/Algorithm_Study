i=0
while True:
    a, b, c = map(int, input().split())
    i +=1
    if a == 0 and b == 0 and c == 0:
        break
    answer = (c//b)*a + min(c%b, a)
    print(f'Case {i}: {answer}')