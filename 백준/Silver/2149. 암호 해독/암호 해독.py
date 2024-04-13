import sys
input = sys.stdin.readline

key = input().strip()
secret = input().strip()
n = len(key)
n_per = len(secret) // n

key_number = [[key[i],i] for i in range(n)]
key_number.sort()
for i in range(0,n):
    key_number[i].append(secret[i*n_per:(i+1)*n_per])

key_number = sorted(key_number, key = lambda x : x[1])

original = ""
for i in range(n_per):
    for j in key_number:
        a,b,word = j
        original += word[i]
print(original)