import sys
import math
input=sys.stdin.readline
def helper0(s,l, r, order):
    if l>r:
        return
    m=(l+r)//2
    order.append(s[m])
    helper0(s,l,m-1, order)
    helper0(s, m+1,r, order)
n = int(input())
s=list(map(int, input().split()))
order=[]
helper0(s,0, n-1, order)
print(*order)
