import sys
input = sys.stdin.readline

word = input()

count0 = word.count('0') // 2
count1 = (len(word) - count0 * 2) // 2
word0 = '0'
word1 = '1'

if len(word) % 4 == 0:
    count = len(word) // 4
    new = word0 * count + word1 * count
else:
    new = word0 * count0 + word1*count1
print(new)