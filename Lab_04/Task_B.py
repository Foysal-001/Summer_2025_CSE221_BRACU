import sys
input=sys.stdin.readline
n,m=map(int, input().split())
u=list(map(int, input().split()))
v=list(map(int, input().split()))
w=list(map(int, input().split()))
ll=[[] for _ in range(n+1)]
for i in range(m):
    st=u[i]
    mid= v[i]
    wg=w[i]
    ll[st].append((mid, wg))
for j in range(1, n + 1):
    print(f"{j}:", end="")
    for a,b in ll[j]:
        print(f"({a},{b})",end="")
    print()  