import sys
input = sys.stdin.readline

while True:
    string = input()
    if string.rstrip() == ".":
        break
    mystring = ""
    for i in string:
        if i.isalpha() or i == "." or  i == " ":
            continue
        mystring += i

    if not mystring:
        print("yes")
    else:
        for _ in range(len(mystring)//2):
            if "()" in mystring:
                mystring = mystring.replace("()","")
            if "[]" in mystring:
                mystring = mystring.replace("[]","")
        if mystring.strip() == "":
            print("yes")
        else:
            print("no")