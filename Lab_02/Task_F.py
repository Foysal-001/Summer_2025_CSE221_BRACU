import sys
input= sys.stdin.readline
n,k=map(int, input().split())
s=list(map(int,input().split()))
count=[0]*999999
a=0
b=0
res=0
if len(set(s)) ==1 and k==1:
    print(n)
else:
    for i in range(n):
        if count[s[i]]==0:
            b+=1
        count[s[i]]+=1
        while b>k:
            count[s[a]]-=1
            if count[s[a]]==0:
                b-=1
            a+=1
        res=max(res,i-a+1)
    print(res)