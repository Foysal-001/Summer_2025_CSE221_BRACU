import sys
from collections import deque
input=sys.stdin.readline
n,m,s,d=map(int,input().split())
ll=[[] for _ in range(n+1)]
if m>0:
    u=list(map(int,input().split()))
    v=list(map(int,input().split()))
    for i in range(m):
        ll[u[i]].append(v[i])
        ll[v[i]].append(u[i])
for i in range(1,n+1):
    ll[i].sort()   
des=[-1]*(n+1)
pre=[-1]*(n+1)
q=deque([s])
des[s]=0
while q:
    x=q.popleft()
    if x==d: break
    for i in ll[x]:
        if des[i]==-1:
            des[i]=des[x]+1
            pre[i]=x
            q.append(i)
if des[d]==-1:
    print(-1)
else:
    print(des[d])
    short=[]
    cur=d
    while cur!=-1:
        short.append(cur)
        cur=pre[cur]
    print(*short[::-1])
