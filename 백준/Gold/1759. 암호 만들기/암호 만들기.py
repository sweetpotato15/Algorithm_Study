import sys
input = sys.stdin.readline

L, C = map(int, input().split())
alpha = sorted(list(input().split()))
# moeum = ['a','e','i','o','u']
# m_count = [1 for x in alpha if x in moeum ]
# if sum(m_count) < 1 or C - sum(m_count) < 2:
#     answer = ''

def dfs(n,st):
    global answer
    if n == C:
        if len(st) == L:
            value = st.count('a') + st.count('e') + st.count('i') + st.count('o') + st.count('u')
            if 1<= value <= L-2:
                answer.append(st)
        return 
    
    dfs(n+1, st+str(alpha[n]))
    dfs(n+1, st)

answer = []
dfs(0,'')
for s in answer:
    print(*s, sep='')
