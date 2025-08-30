import sys
import heapq
input=sys.stdin.readline
n,m,s,d=map(int, input().split())
u=list(map(int, input().split()))
v=list(map(int, input().split()))
w=list(map(int, input().split()))
ll=[[] for _ in range(n+1)]
for i in range(m):
    ll[u[i]].append((v[i], w[i]))
llongg=10**18
l=[llongg] * (n+1)
src=[-1]*(n+1)
l[s]=0
pq=[(0,s)]  
while pq:
    cur,node=heapq.heappop(pq)
    if cur>l[node]:
        continue
    for i, j in ll[node]:
        if l[i]>cur+j:
            l[i]=cur+j
            src[i]=node
            heapq.heappush(pq,(l[i],i))
if l[d]==llongg:
    print(-1)
else:
    print(l[d])
    shortest=[]
    cur=d
    while cur !=-1:
        shortest.append(cur)
        cur=src[cur]
    shortest.reverse()
    print(*shortest)
