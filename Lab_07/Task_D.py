import sys
import heapq
input=sys.stdin.readline
n,m,s,d=map(int, input().split())
wait=[0]+list(map(int, input().split()))  
ll=[[] for _ in range(n + 1)]
for i in range(m):
    u,i=map(int, input().split())
    ll[u].append(i)
INF=10**18
l=[INF]*(n+1)
l[s]=wait[s]
pq=[(l[s],s)] 
while pq:
    cost,u=heapq.heappop(pq)
    if cost>l[u]:
        continue
    for i in ll[u]:
        cost2=cost+wait[i]
        if cost2<l[i]:
            l[i]=cost2
            heapq.heappush(pq,(cost2,i))
if l[d]==INF:
    print(-1)
else:
    print(l[d])
