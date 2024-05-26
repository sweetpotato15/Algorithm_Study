from collections import Counter
def solution(str1, str2):
    A = [str1[i:i+2].lower() for i in range(len(str1)-1) if str1[i:i+2].isalpha()]
    B = [str2[i:i+2].lower() for i in range(len(str2)-1) if str2[i:i+2].isalpha()]

    A1 = Counter(A)
    B1 = Counter(B)
    
    up = sum((A1&B1).values())
    down = sum((A1|B1).values())
    
    if down == 0: return 65536
    else: return int((up/down)*65536)