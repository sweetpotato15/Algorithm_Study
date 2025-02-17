array = list(input().strip())
if '0' not in array:
    print(-1)
else:
    array = [int(x) for x in array]
    if sum(array) % 3 != 0:
        print(-1)
    else:
        array = sorted(array, reverse=True)
        array = [str(x) for x in array]
        answer = ''.join(array)
        print(answer)