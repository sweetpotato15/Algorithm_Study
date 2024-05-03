import sys
input = sys.stdin.readline

word = input()
word0 = '0'
word1 = '1'

# new에 필요한 0,1개수
count0 = word.count('0') // 2 
count1 = (len(word) - count0 * 2) // 2
count = 0 # 1을 몇개 pass 할건지

new = ''
for i in range(len(word)):
    if len(new) == len(word) // 2:
        break
    if word[i] == '0' and count0 >0:
        new += word0
        count0 -= 1
    elif count < count1: # 1을 pass 하는 경우우
        count += 1
        continue
    else:
        new += word1

print(new)