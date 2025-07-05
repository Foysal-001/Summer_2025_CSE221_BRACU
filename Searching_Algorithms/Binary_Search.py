n=list(map(int, input().split()))
n.sort()
target=int(input())
left=0
right= len(n)-1
flag=False
while left <=right:
    mid=(left+right)//2
    if n[mid] == target:
        print(n[mid])
        flag=True
        break

    elif n[mid] > target:
        right = mid-1

    else:
        left = mid+ 1

if flag==False:
    print('NOT FOUND')

    