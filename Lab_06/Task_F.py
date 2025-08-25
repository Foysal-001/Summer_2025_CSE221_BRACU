import sys
input=sys.stdin.readline
from collections import deque
import time
t=time.time()
n,m,s,q=map(int, input().split())
ll=[[] for _ in range(n + 1)]
for i in range(m):
    u,v=map(int, input().split())
    ll[u].append(v)
    ll[v].append(u)
src=list(map(int, input().split()))
des=list(map(int, input().split()))
l=[-1]*(n+1)
q=deque()
for src in src:
    l[src]=0
    q.append(src)
while q:
    gg=q.popleft()
    for i in ll[gg]:
        if l[i]==-1:   
            l[i]=l[gg] + 1
            q.append(i)
res=[]
for d in des:
    res.append((l[d]))
print(*res)
e=time.time()

print(e-t)