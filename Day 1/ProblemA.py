import heapq
file = open('Day 1\input.txt','r')

l = []
r = []

for s in file.readlines():
    x,y = s.split()
    heapq.heappush(l, int(x))
    heapq.heappush(r, int(y))

ans = 0
while l and r:
    ans += abs(heapq.heappop(l) - heapq.heappop(r))

print(ans)