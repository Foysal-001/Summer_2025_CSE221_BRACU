'''Fast Modular Exponentiation 
This method is also known as Binray exponentiation. It is used to find the remainder of two large number powered to each other 
like a=10^18 and b=10^12 you are asked to find a^b%(a given integer) in this case tradition method fails to compute as the number
get unusually large. But here binary exponentiation walks in and solves it in a fraction of time because Binary exponentiation solves 
this problem in O(log_b) time complexity!!'''

import sys
input=sys.stdin.readline
a,b=map(int, input().split())
mod=int(input())
rem=1
a%=mod
while b:
    if b % 2:
        rem=rem*a%mod
    a=a*a%mod
    b= b//2
print(rem)
