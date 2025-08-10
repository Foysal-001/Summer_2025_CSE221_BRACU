import sys
input=sys.stdin.readline
n,m,k=map(int, input().split())
kn=set()
for i in range(k):
    x, y = map(int, input().split())
    kn.add((x,y))
possible=[(2,1), (2,-1), (-2,1), (-2,-1),(1,2), (1,-2), (-1,2), (-1,-2)]
flag=False
for (x,y) in kn:
    for i,j in possible:
        p,q= x+i, y+j
        if (p,q) in kn:
            flag = True
            break
    if flag:
        break
print("YES" if flag else "NO")
