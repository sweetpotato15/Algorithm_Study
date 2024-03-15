a,b,c = map(int, input().split())
if a == b:
    if a == c: # a = b = c 222
        score = 10000 + a * 1000
    else: # a = b != c 224 
        score = 1000 + a * 100
else: 
    if a == c: # 242
        score = 1000 + a * 100
    elif b == c : # 233
        score = 1000 + b * 100
    else: # 234
        score = max(a,b,c) * 100
        
print(score)