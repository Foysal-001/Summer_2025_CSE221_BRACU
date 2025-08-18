import sys
import math
from collections import deque
input=sys.stdin.readline
n,m=map(int, input().split())
ll=[[] for _ in range(n+1)]
for j in range(m):
    u,v=map(int, input().split())
    ll[u].append(v)
    ll[v].append(u)
visit=[False]*(n+1)
q=deque()
order=[]
q.append(1)
visit[1]=True
while q:
    city=q.popleft()
    order.append(city)
    for j in ll[city]:
        if  visit[j] == False:
            visit[j] = True
            q.append(j)
print(*order)



