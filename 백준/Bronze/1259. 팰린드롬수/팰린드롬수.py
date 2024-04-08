while True:
    a = input()
    if int(a) == 0:
        break

    if int(a) == int(a[::-1]):
        print("yes")
    else:
        print("no")