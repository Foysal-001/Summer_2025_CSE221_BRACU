#Fast Exponentiation (binary exponentiation)
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