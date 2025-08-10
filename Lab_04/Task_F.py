import sys
input=sys.stdin.readline
n = int(input())
x, y = map(int, input().split())
possible = [(-1, -1), (-1, 0), (-1, 1),(0, -1),(0, 1),(1, -1),(1, 0),(1, 1)]
ll = []
for i, j in possible:
    p,q=x +i, y+j
    if 1<=p<=n and 1<=q <=n:
        ll.append((p,q))
ll.sort()
print(len(ll))
for a,b in ll:
    print(a,b)
