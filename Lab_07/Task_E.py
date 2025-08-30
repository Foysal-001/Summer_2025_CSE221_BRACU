import sys
import heapq
input=sys.stdin.readline
n,m=map(int, input().split())
u=list(map(int, input().split()))
v=list(map(int, input().split()))
w=list(map(int, input().split()))
ll=[[] for _ in range(n + 1)]
for i in range(m):
    ll[u[i]].append((v[i], w[i]))
INF=10**18
l=[[INF, INF] for _ in range(n + 1)]
pq=[]
for i,j in ll[1]:
    p=j%2
    if j<l[i][p]:
        l[i][p]=j
        heapq.heappush(pq,(j, i, p))
while pq:
    cost,node,parity=heapq.heappop(pq)
    if cost>l[node][parity]:
        continue
    for i, j in ll[node]:
        parity2=j%2
        if parity2==parity:  
            continue
        cost2=cost+j
        if cost2<l[i][parity2]:
            l[i][parity2]=cost2
            heapq.heappush(pq,(cost2,i,parity2))
ans=min(l[n][0],l[n][1])
if ans!=INF:
    print(ans)
else:
    print(-1)
