import sys
import heapq
input = sys.stdin.readline
n,m,s,d=map(int, input().split())
ll=[[] for _ in range(n + 1)]
for i in range(m):
    u,i,j=map(int, input().split())
    ll[u].append((i, j))
    ll[i].append((u, j))  
INF=10**18
l1=[INF]*(n+1)
l2=[INF]*(n+1)
l1[s]=0
pq = [(0,s)]  
while pq:
    cost,u=heapq.heappop(pq)
    if cost>l2[u]:
        continue
    for i,j in ll[u]:
        cost2=cost + j
        if cost2<l1[i]:
            l2[i]=l1[i]
            l1[i]=cost2
            heapq.heappush(pq,(cost2, i))
        elif l1[i]<cost2<l2[i]:
            l2[i]=cost2
            heapq.heappush(pq,(cost2,i))
if l2[d]!=INF:
    print(l2[d])
else:
    print(-1)

