import sys
input=sys.stdin.readline
sys.setrecursionlimit(999999)
n,m=map(int,input().split())
u=list(map(int,input().split()))
v=list(map(int,input().split()))
ll = [[] for _ in range(n+1)]
for i in range(m):
    ll[u[i]].append(v[i])
    ll[v[i]].append(u[i])
visit=[False]*(n+1)
order=[]
def pseudodfs(a):
    visit[a]=True
    order.append(a)
    for i in ll[a]:
        if not visit[i]:
            pseudodfs(i)
pseudodfs(1)
print(*order)
