from collections import Counter

file = open('Day 1\input.txt','r')
c = Counter()

l = []

for s in file.readlines():
    x, y = s.split()
    c[int(y)] += 1
    l.append(int(x))

ans = 0

for x in l:
    ans += x * c[x]

print(ans)