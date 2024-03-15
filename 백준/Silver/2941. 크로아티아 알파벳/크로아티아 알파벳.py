n = (input())

croatia_alphabet = ["c=","c-","dz=","d-","lj","nj","s=","z="]
for i in croatia_alphabet:
    n = n.replace(i, "?")

print(len(n))
