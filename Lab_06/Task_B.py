import sys
from collections import deque
input=sys.stdin.readline
n,m=map(int, input().split())
ll=[[] for _ in range(n + 1)]
for i in range(m):
    u,v=map(int, input().split())
    ll[u].append(v)
    ll[v].append(u)
visit=[False]*(n+1)
count=0
for i in range(1, n+1):
    if not visit[i]:
        q=deque()
        q.append((i,0))  
        visit[i]=True
        color=[0,0]
        color[0]+=1
        while q:
            node,col=q.popleft()
            for nei in ll[node]:
                if not visit[nei]:
                    visit[nei]=True
                    new_col=1-col
                    color[new_col]+=1
                    q.append((nei,new_col))
        count+=max(color)
print(count)