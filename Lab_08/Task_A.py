'''import sys
input=sys.stdin.readline
n,k=map(int, input().split())
ll=[i for i in range(n+1)]
res=[1]*(n+1)
for i in range(k):
    a,b=map(int, input().split())
    x=a
    while ll[x]!=x:
        ll[x]=ll[ll[x]] 
        x=ll[x]
    hedA=x
    y=b
    while ll[y]!=y:
        ll[y]=ll[ll[y]]  
        y=ll[y]
    hedB=y
    if hedA!=hedB:
        if res[hedA]<res[hedB]:
            hedA,hedB=hedB, hedA
        ll[hedB]=hedA
        res[hedA]+=res[hedB]
    print(res[hedA])'''


n,k=map(int,input().split());p=list(range(n+1));s=[1]*(n+1)
for _ in range(k):a,b=map(int,input().split());f=lambda x:f(p[x]) if p[x]!=x else x;ra,rb=f(a),f(b);[p.__setitem__(rb,ra),s.__setitem__(ra,s[ra]+s[rb])] if ra!=rb else None;print(s[f(ra)])
