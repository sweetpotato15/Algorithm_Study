from collections import Counter
from math import ceil
array = Counter(list(input()))

num = array['6'] + array['9']
array['6'] = 0
array['9'] = 0

answer = max(array.values())
answer = max(answer, ceil(num/2))
print(answer)