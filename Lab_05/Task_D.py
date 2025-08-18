import sys
from collections import deque
input=sys.stdin.readline
n,m,s,d,k=map(int, input().split())
ll=[[] for _ in range(n+1)]
for i in range(m):
    u,v=map(int,input().split())
    ll[u].append(v)

def bfs_trav(root):
    l=[-1]*(n+1)
    pre=[-1]*(n+1)
    q=deque([root])
    l[root]=0
    while q:
        x=q.popleft()
        for i in ll[x]:
            if l[i]==-1:
                l[i]=l[x]+1
                pre[i]=x
                q.append(i)
    return l,pre
d_s,p_s=bfs_trav(s)
d_k,p_k=bfs_trav(k)

if d_s[k]==-1 or d_k[d]==-1:
    print(-1)
else:
    s_path=[]
    x=k
    while x!=-1:
        s_path.append(x)
        x=p_s[x]
    s_path=s_path[::-1]
    x=d
    tmp=[]
    while x!=-1:
        tmp.append(x)
        x=p_k[x]
    if tmp and tmp[0]==k:
        tmp=tmp[1:]  
    s_path+=tmp

    print(len(s_path)-1)
    print(*s_path)
