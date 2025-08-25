import sys
input=sys.stdin.readline
n=int(input())
s=[input().strip() for _ in range(n)]
char=set()
for i in s:
    for c in i:
        char.add(c)
ll={c:[] for c in char}
deg={c: 0 for c in char}
flag=True
for i in range(n-1):
    w1,w2=s[i],s[i+1]
    minlen = min(len(w1), len(w2))
    f=False
    for j in range(minlen):
        if w1[j]!=w2[j]:
            ll[w1[j]].append(w2[j])
            deg[w2[j]]+=1
            f=True
            break
    if not f and len(w1)>len(w2):
        flag=False
        break
if not flag:
    print(-1)
else:
    total=[]
    for c in char:
        if deg[c]==0:
            total.append(c)
    res=[]
    while total:
        total.sort()
        u=total.pop(0)
        res.append(u)
        for v in ll[u]:
            deg[v]-=1
            if deg[v]==0:
                total.append(v)
    if len(res)!=len(char):
        print(-1)
    else:
        print("".join(res))
