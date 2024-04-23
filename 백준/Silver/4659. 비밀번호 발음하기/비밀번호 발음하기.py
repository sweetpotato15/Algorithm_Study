import sys
input = sys.stdin.readline

wordlist = ["a","e","i","o","u"]
def check_word(word):
    if word in wordlist:
        return 1 # 모음이면 1
    return 2 # 자음이면 2

while True:
    word = input().strip()
    if word == 'end':
        break
    answer = "acceptable"
    count1, count2, count = 0,0,0 # 각 모음 개수, 자음 개수, 전체 모음 개수
    
    for i in range(len(word)):
        if check_word(word[i]) == 1: # 모음이면
            count += 1
            count1 += 1
            count2 = 0
        else : # 자음이면
            count1 = 0 
            count2 += 1
        if count1 >= 3 or count2 >= 3:
            answer = "not acceptable"
            break
        if count1 == 2 :
            if word[i] == word[i-1] and word[i] not in ["e","o"]:
                answer = "not acceptable"
                break
        if count2 == 2:
            if word[i] == word[i-1]:
                answer = "not acceptable"
                break
    if count == 0:
        answer = "not acceptable"
    print("<{}> is {}.".format(word, answer))