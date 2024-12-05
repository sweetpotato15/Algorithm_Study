def is_right(s): # 괄호 문자열이 올바른지 return 해주는 함수
    while '[]' in s or '{}' in s or '()' in s:
        if '[]' in s:
            s = s.replace('[]','')
        elif '()' in s:
            s = s.replace('()','')
        else:
            s = s.replace('{}', '')
    if s:
        return False
    else:
        return True
    
def solution(s):
    d_s = s*2
    answer = 0
    for i in range(len(s)):
        x = d_s[i:i+len(s)]
        answer += is_right(x)
    return answer