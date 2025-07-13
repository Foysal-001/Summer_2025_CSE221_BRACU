import sys
input= sys.stdin.readline
n,x=map(int,input().split())
a=list(map(int,input().split()))
s=[(a[i],i+1) for i in range(n)]  
s.sort()
for i in range(n):
  l=i+1
  r=n-1
  while l<r:
    total=s[i][0]+s[l][0]+s[r][0]
    if total==x:
      print(s[i][1],s[l][1],s[r][1])
      exit(0)
    elif total<x:
      l+=1
    else:
      r-=1
print('-1')
