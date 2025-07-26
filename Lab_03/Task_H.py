import sys
input=sys.stdin.readline
n=int(input())
io=list(map(int, input().split()))
post=list(map(int, input().split()))
pre=[n-1]
def dnjkfasdjkfhajf(l, r):
    if l>r:
        return []
    root=post[pre[0]]
    pre[0]-=1
    idx=-1
    for i in range(l, r + 1):
        if io[i]==root:
            idx=i
            break
    right= dnjkfasdjkfhajf(idx+1, r)
    left= dnjkfasdjkfhajf(l,idx-1)
    return [root]+ left +right

res= dnjkfasdjkfhajf(0, n - 1)
print(*res)