import sys
from collections import deque
input=sys.stdin.readline
n,m=map(int,input().split())
ll=[[] for _ in range(n+1)]
visit=[0]*(n+1)
for i in range(m):
    a,b=map(int,input().split())
    ll[a].append(b)
    visit[b]+=1
q=deque()
for i in range(1,n+1):
    if visit[i]==0:
        q.append(i)
res=[]
while q:
    u=q.popleft()
    res.append(u)
    for v in ll[u]:
        visit[v]-=1
        if visit[v]==0:
            q.append(v)
if len(res)!=n:
    print(-1)
else:
    print(*res)
