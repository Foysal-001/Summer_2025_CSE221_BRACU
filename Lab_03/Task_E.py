import math 
import sys
input=sys.stdin.readline
for i in range(int(input())):
    a,n,m=map(int,input().split())
    if a==1:
        print(n%m)
        continue
    num=(power(a,n+1,m*a-1)-a)% (m*a-1)
    inv=(a-1)
    while inv%2==0 and m%2==0:
        inv//=2
        m//=2
    inv=power(inv,m-2,m)  
    print((num*inv)%m)

    
def power(a,b,m):
    res=1
    a%=m
    while b:
        if b%2== 1:
            res=(res*a)%m
        a=(a*a)%m
        b=b// 2
    return res