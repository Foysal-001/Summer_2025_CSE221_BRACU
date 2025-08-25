import sys
input=sys.stdin.readline
from collections import deque
n=int(input())
ll=[[] for _ in range(n + 1)]
for i in range(n-1):
    u,v=map(int, input().split())
    ll[u].append(v)
    ll[v].append(u)
    
def bfs(a):
    visit=[False] * (n + 1)
    l=[0]*(n+1)
    q=deque()
    q.append(a)
    visit[a]=True
    far_node=a
    while q:
        node=q.popleft()
        for i in ll[node]:
            if not visit[i]:
                visit[i]=True
                l[i]=l[node]+1
                q.append(i)
                if l[i]>l[far_node]:
                    far_node=i
    return far_node,l[far_node]
A,_=bfs(1)
B,length=bfs(A)
print(length)
print(A,B)
