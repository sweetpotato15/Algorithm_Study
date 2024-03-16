n = int(input())

def groupword(word):
    only = []
    only.append(word[0])
    for i in range(len(word)-1):
        if word[i] != word[i+1]:
            only.append(word[i+1])
        
    if len(only) == len(set(only)):
        return 1
    else:
        return 0
    
answer = 0
for _ in range(n):
    answer += groupword(input())

print(answer)

            
