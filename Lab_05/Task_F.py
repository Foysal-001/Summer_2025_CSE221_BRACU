import sys
sys.setrecursionlimit(2*100000+5)
from collections import deque
import math
input=sys.stdin.readline
n,m=map(int,input().split())
ll=[[] for _ in range(n+1)]
for i in range(m):
    u,v=map(int,input().split())
    ll[u].append(v)
visit=[0]*(n+1)  
cycle=False
for i in range(1,n+1):
    if visit[i]:
        continue
    
    stk=[i]
    pt=[]
    while stk:
        x=stk[-1]
        if visit[x]==0:
            visit[x]=1
            pt.append(x)
            for y in ll[x]:
                if visit[y]==0:
                    stk.append(y)
                elif visit[y]==1:
                    cycle=True
                    #stk.clear()
                    break
        else:
            stk.pop()
            if visit[x]==1:
                visit[x]=2
    if cycle: 
        break
print("YES" if cycle else "NO")
