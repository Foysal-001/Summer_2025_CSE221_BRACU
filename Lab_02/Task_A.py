'''#Time scaling
import sys
input= sys.stdin.readline
n,s=map(int, input().split())
a=list(map(int, input().split()))
for i in range(n):
    for j in range(i+1,n):
        flag=True
        if a[i] + a[j] == s:
                print(i+1,j+1)
                flag=False
                break
        else:
            continue

    if flag == False:
        break
if flag == False:
    pass

else:
    print('-1')'''

import sys
input= sys.stdin.readline
n, s = map(int, input().split())
a = list(map(int, input().split()))
st = 0
end = n - 1
flag=False
while st < end:
    total = a[st] + a[end]
    if total == s:
        print(st + 1, end + 1)
        flag = True
        break          
    elif total < s:
            st += 1
    else:
            end -= 1
if flag == False:  
    print(-1)

