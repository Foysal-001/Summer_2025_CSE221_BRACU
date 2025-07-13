import sys
input= sys.stdin.readline
n,k=map(int,input().split())
s=list(map(int,input().split()))
a=0
b=0
count=0
if sum(s) <= k:
    print(n)
    exit(0)
for i in range(n):
  b+=s[i]
  while b>k:
    b-=s[a]
    a+=1
  if i-a+1>count:
    count=i-a+1
print(count)
