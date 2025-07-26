'''#Fast Exponentiation (binary exponentiation)
import sys
input=sys.stdin.readline
a,b=map(int, input().split())
mod=107
rem=1
a%=mod
while b:
    if b % 2:
        rem=rem*a%mod
    a=a*a%mod
    b= b//2
print(rem)
'''
import sys
input=sys.stdin.readline
def merg(s):
    def lab3(low,right):
        if right-low<=1:
            return 0
        m=(low+right)//2
        gg=lab3(low,m)+lab3(m, right)
        ll=[]
        i,j= low,m
        while i<m and j<right:
            if s[i]<=s[j]:
                ll.append(s[i])
                i += 1
            else:
                ll.append(s[j])
                gg+=m-i
                j+=1
        while i<m:
            ll.append(s[i])
            i+=1
        while j<right:
            ll.append(s[j])
            j+=1
        s[low:right]=ll
        return gg
    return lab3(0,len(s))


n=int(input())
a=list(map(int, input().split()))
count=merg(a)
print(count)
print(*a)
