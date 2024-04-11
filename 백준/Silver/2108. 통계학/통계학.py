import sys

n=int(sys.stdin.readline())
num=[]
dic_num={}
cnt=0
cnt2=0

for i in range(n):
  k=int(sys.stdin.readline())
  if k not in dic_num:
    dic_num[k]=1
  else:
    dic_num[k]+=1
  num.append(k)
  cnt+=k

num.sort()
maxnum=max(dic_num.values())

for i in sorted(set(num)):
  if dic_num[i]==maxnum:
    modenum=i
    cnt2+=1
  if cnt2==2:
    break

print(round(cnt/n)) #n=홀수
print(num[n//2])
print(modenum)
print(num[n-1]-num[0])