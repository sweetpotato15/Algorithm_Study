
s = input()
t = input()

answer = 0

def ab2(s, t):
  global answer
  if len(s) == len(t):
    if s == t:
      answer = 1
    return 
  if t[-1] == "A":
    ab2(s, t[:-1])
  if t[0] == "B":
    t = t[1:]
    ab2(s, t[::-1])

ab2(s,t)
print(answer)
