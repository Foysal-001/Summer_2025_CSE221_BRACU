import sys
input=sys.stdin.readline
n,m=map(int, input().split())
u=list(map(int, input().split()))
v=list(map(int, input().split()))
ll=[0]*n
for i in range(m):
    ll[v[i]-1]+=1   
    ll[u[i]-1]-=1   
for j in ll:
    print(j, end=" ")
