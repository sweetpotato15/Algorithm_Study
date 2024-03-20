n = int(input())

def recursion(string, start, end):
    global count
    count += 1
    if start >= end :
        return 1
    elif string[start] != string[end]:
        return 0
    else:
        return recursion(string, start+1, end-1)
    
def isPalindrome(string):
    return recursion(string, 0, len(string)-1)

for _ in range(n):
    count = 0
    print(isPalindrome(input()), count)