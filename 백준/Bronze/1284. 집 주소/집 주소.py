while True:
    command = list(input().strip())
    ans = 1
    if command[0] == "0":
        break
    for i in command:
        ans += 1
        if int(i) == 1:
            ans += 2
        elif int(i) == 0:
            ans += 4
        else:
            ans += 3
    print(ans)