import sys
import heapq
from collections import deque
input=sys.stdin.readline
def dijk(st,ll,n):
    l=[10**18]*(n+1)
    l[st]=0
    h=[(0,st)]
    while h:
        d,u=heapq.heappop(h)
        if d>l[u]:continue
        for v,w in ll[u]:
            if d+w<l[v]:
                l[v]=d+w
                heapq.heappush(h,(l[v],v))
    return l
n,m,s,t=map(int,input().split())
ll=[[] for _ in range(n+1)]
for i in range(m):
    u,v,w=map(int,input().split())
    ll[u].append((v,w))
al=dijk(s,ll,n)
bob=dijk(t,ll,n)
best=10**18
des=-1
for i in range(1,n+1):
    if al[i]<10**18 and bob[i]<10**18:
        met=max(al[i],bob[i])
        if met<best or (met==best and i<des):
            best,des=met,i
print(-1 if des==-1 else f"{best} {des}")
