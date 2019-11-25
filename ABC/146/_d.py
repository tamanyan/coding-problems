import sys
import math
from bisect import bisect_right as br
from bisect import bisect_left as bl
sys.setrecursionlimit(1000000)
from heapq import heappush, heappop,heappushpop
from collections import defaultdict
from itertools import accumulate
from collections import Counter
from collections import deque
from operator import itemgetter
from itertools import permutations
mod = 10**9 + 7
inf = float('inf')
def I(): return int(sys.stdin.readline())
def LI(): return list(map(int,sys.stdin.readline().split()))

n = I()
graph = [[] for _ in range(n)]
edge = []
for i in range(n-1):
    a,b = LI()
    a -= 1
    b -= 1
    graph[a].append((b,i))
    graph[b].append((a,i))
    edge.append((a,b,i))

m = 0
for i in range(n):
    m = max(m,len(graph[i]))

print(m)
ans = [None]*(n-1)
que = deque()
que.append((0,0))
while que:
    v,color = que.popleft()
    cnt = 1
    for u,i in graph[v]:
        if ans[i] == None:
            if cnt != color:
                ans[i] = cnt
                que.append((u,cnt))
                cnt += 1
            else:
                ans[i] = cnt+1
                que.append((u,cnt+1))
                cnt += 2
print(*ans)
