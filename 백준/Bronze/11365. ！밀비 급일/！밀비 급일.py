while True:
    string = input().strip()
    if string == "END":
        break
    print(string[::-1])