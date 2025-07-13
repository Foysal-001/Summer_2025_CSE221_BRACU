'''import sys
input = sys.stdin.readline
n,m,k=map(int, input().split())
a=list(map(int, input().split()))
b=list(map(int, input().split()))
count=99999999999999999
c1,c2=0,0
flag=True
for i in range(n):
    for j in range(m):
        if abs(a[i]+b[j]-k) < count:
            count=abs(a[i]+b[j]-k)
            c1=i
            c2=j
        if count==0:
            flag=False
            break
        else:
            continue


    if flag == False:
        break


print(c1+1,c2+1)'''



import sys
input = sys.stdin.readline
n,m,k=map(int,input().split())
a=list(map(int,input().split()))
b=list(map(int,input().split()))
count=99999999999999999
c1,c2=0,0
i,j=0,m-1
while i<n and j>= 0:
    total=a[i]+ b[j]
    diff=abs(total-k)
    if diff<count:
        count=diff
        c1,c2=i,j
        
    if total>k:
        j-=1

    elif total<k:
        i+=1


    else:
 
        break  
print(c1+1,c2+1)

