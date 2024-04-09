
t = int(input())

def VPS():
    word = input()
    if word.count("(") != word.count(")"):
        print("NO")
    else:
        left ,right = 0,0
        for i in word:
            if i == '(':
                left += 1
            else:
                right += 1
            
            if left < right:
                answer = "NO"
                break
            answer = "YES"
        print(answer)

for i in range(t):
    VPS()
