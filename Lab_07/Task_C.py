import sys
import heapq
input=sys.stdin.readline
n,m=map(int, input().split())
ll=[[] for _ in range(n+1)]
for i in range(m):
    u,i,j=map(int, input().split())
    ll[u].append((i,j))
    ll[i].append((u,j))
INF=10**9+7
bad=[INF]*(n+1)
bad[1]=0
pq=[(0,1)] 
while pq:
    d,u=heapq.heappop(pq)
    if d>bad[u]:
        continue
    for i,j in ll[u]:
        new=max(d, j)
        if new<bad[i]:
            bad[i]=new
            heapq.heappush(pq,(new,i))
res=[]
for i in range(1,n+1):
    if bad[i]!=INF:
        res.append(str(bad[i]))
    else:
        res.append(str(-1))
print(*res)