from collections import Counter

def solution(want, number, discount):
    want_dict = {i:j for i,j in zip(want, number)}
    ans = 0

    for i in range(len(discount)-10+1):
        flag = True
        counter = dict(Counter(discount[i:i+10]))

        if set(want)-set(counter.keys()): # want에 있는데 discount에 없는 경우 
            continue
        else:
            for j in want:
                if counter[j] < want_dict[j]:
                    flag = False
                    continue
        if flag:
            ans += 1
    return ans
