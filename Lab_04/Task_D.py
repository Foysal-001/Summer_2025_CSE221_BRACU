import sys
input=sys.stdin.readline
n,m=map(int, input().split())
u=list(map(int, input().split()))
v=list(map(int, input().split()))
ll=[0]*(n+1)
for i in range(m):
    ll[u[i]]+=1
    ll[v[i]]+=1
odd=0
for i in ll:
    if i%2==1:
        odd+=1

if odd==0 or odd==2:
    print("YES")
else:
    print("NO")
