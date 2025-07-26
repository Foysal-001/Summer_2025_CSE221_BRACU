import sys
input=sys.stdin.readline
n=int(input())
io=list(map(int, input().split()))
pro=list(map(int, input().split()))
post=[0]
def dnjkfasdjkfhajf(l, r):
    if l>r:
        return []
    root=pro[post[0]]
    post[0]+=1    
    idx=-1
    for i in range(l,r+1):
        if io[i]==root:
            idx=i
            break
    left=dnjkfasdjkfhajf(l,idx-1)
    right=dnjkfasdjkfhajf(idx+1, r)
    return left + right+  [root]

res=dnjkfasdjkfhajf(0,n-1)
print(*res)
