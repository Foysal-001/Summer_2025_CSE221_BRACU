'''
import sys
input= sys.stdin.readline
n,q=map(int, input().split())
s=list(map(int, input().split()))
l1=[]
l2=[]
for i in range(q):
    a,b=map(int, input().split())
    l1.append(a)
    l2.append(b)


for j in range(q):
    diff= l2[j]-l1[j]
    if diff > s[-1]:
        print(n)

    else:
        count=0
        for k in range(n):
           if s[k] >= l1[j] and s[k] <= l2[j]:
               count+=1

           elif s[k] > l2[j]:
               print(count)
               break'''
           
           

import sys
input = sys.stdin.readline

n, q = map(int, input().split())
s = list(map(int, input().split()))

l1 = []
l2 = []

for _ in range(q):
    a, b = map(int, input().split())
    l1.append(a)
    l2.append(b)

for j in range(q):
    x = l1[j]
    y = l2[j]
    low = 0
    high = n
    while low < high:
        mid = (low + high) // 2
        if s[mid] < x:
            low = mid + 1
        else:
            high = mid
    left = low
    low = 0
    high = n
    while low < high:
        mid = (low + high) // 2
        if s[mid] <= y:
            low = mid + 1
        else:
            high = mid
    right = low

    print(right - left)


















'''for i in range(q):
    a,b=map(int, input().split())
    diff=b-a
    if diff > s[-1] and a<=s[0]:
        print(n)
    else:
        count=0
        for j in range(n):
            if s[j] >= a and s[j] <=b:
                count+=1
            elif s[j] > b:
                print(count)
                break'''








