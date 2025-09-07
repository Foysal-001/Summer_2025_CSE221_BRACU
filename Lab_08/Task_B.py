import sys
input=sys.stdin.readline
n,m=map(int,input().split())
edges=[]
for _ in range(m):
    u,v,w=map(int,input().split())
    edges.append((w,u,v))
edges.sort()
parent=[i for i in range(n+1)]
size=[1]*(n+1)
total=0
for w,u,v in edges:
    x=u
    while parent[x]!=x:
        parent[x]=parent[parent[x]]
        x=parent[x]
    ru=x
    y=v
    while parent[y]!=y:
        parent[y]=parent[parent[y]]
        y=parent[y]
    rv=y
    if ru!=rv:
        if size[ru]<size[rv]:
            ru,rv=rv,ru
        parent[rv]=ru
        size[ru]+=size[rv]
        total+=w
print(total)
