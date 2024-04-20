import sys
input = sys.stdin.readline

s,p = map(int, input().split())
dna = input().strip()
answerList = list(map(int, input().split()))

mystring = dna[:p]
mylist = []
dnalist = ["A","C","G","T"]

for i in range(4):
    mylist.append(mystring.count(dnalist[i]))

def checkpoint(list1, list2):
    sum = 0
    for i in range(4):
        if list1[i] - list2[i] >=0:
            sum +=1 
    if sum == 4:
        return True
    else:
        return False

count = 0
if checkpoint(mylist, answerList):
    count += 1

for start in range(s-p):

    mylist[dnalist.index(dna[start])] -= 1
    mylist[dnalist.index(dna[start+p])] += 1

    if checkpoint(mylist, answerList):
        count += 1

print(count)