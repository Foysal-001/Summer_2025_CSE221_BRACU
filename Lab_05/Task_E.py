import sys
input=sys.stdin.readline
n,r=map(int,input().split())
ll=[[] for _ in range(n+1)]
for i in range(n-1):
    u,v=map(int,input().split())
    ll[u].append(v)
    ll[v].append(u)
l=[1]*(n+1)
pre=[0]*(n+1)
stk=[r]
order=[]
while stk:
    x=stk.pop()
    order.append(x)
    for y in ll[x]:
        if y!=pre[x]:
            pre[y]=x
            stk.append(y)
for x in reversed(order):
    if pre[x]:
        l[pre[x]]+=l[x]

q=int(input())
out=[]
for i in range(q):
    x=int(input())
    out.append(str(l[x]))
print('\n'.join(out))
