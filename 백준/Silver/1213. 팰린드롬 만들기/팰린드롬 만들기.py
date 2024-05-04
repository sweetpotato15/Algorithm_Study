import sys
input = sys.stdin.readline
name = input().strip() # 입력 
name_value = list(set(list(name))) # name 에 포함된 알파벳 종류
name_value.sort()
name_count = {} # 알파벳 : 개수 dict
for i in name_value:
    name_count[i] = name.count(i)

start = ''
middle = ''
for i in range(len(name_value)):
    count = name_count[name_value[i]]
    start += name_value[i] * (count // 2)
    middle += name_value[i] * (count % 2)

if len(middle) > 1:
    print("I'm Sorry Hansoo")
else:
    print(start+middle+start[::-1])