'''
import sys
input= sys.stdin.readline
for i in range(int(input())):
    k,x=map(int, input().split())
    count=0
    val=0
    while True:
        count+=1
        if count % x !=0:
            val+=1
            if val == k:
                print(count)
                break
            else:
                continue

        else:
            continue
        

import sys
input = sys.stdin.readline

for i in range(int(input())):
    k, x = map(int, input().split())
    res = k + (k - 1) // (x - 1)
    print(res)


import sys
input = sys.stdin.readline
for i in range(int(input())):
    k, x = map(int, input().split())
    a  = (x - 1)
    total = k // a
    count = total * x
    rem = k % a
    if rem == 0:
        count -= 1
    else:
        while rem > 0:
            count += 1
            if count % x != 0:
                rem -= 1
    print(count)
'''

import sys
input= sys.stdin.readline
for i in range(int(input())):
  k,x=map(int,input().split())
  count=1
  a=2*k
  while count<a:
    b=(count+a)//2
    if b - b//x < k:
      count=b+1
    else:
      a=b
  print(count)



