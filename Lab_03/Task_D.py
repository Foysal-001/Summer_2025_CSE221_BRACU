import sys
import math
input=sys.stdin.readline
m = 10**9 + 7
for i in range(int(input())):
    a, b, c, d=map(int, input().split())
    x=int(input())
    mat=[[a,b], [c,d]]
    res=[[1,0], [0,1]]  
    while x>0:
        if x%2==1:
            r00= (res[0][0]* mat[0][0]+ res[0][1] *mat[1][0]) % m
            r01= (res[0][0]* mat[0][1]+res[0][1] *mat[1][1]) % m
            r10= (res[1][0]* mat[0][0]  + res[1][1] *mat[1][0]) % m
            r11= (res[1][0]*mat[0][1] + res[1][1] *mat[1][1]) % m
            res = [[r00, r01], [r10, r11]]
        a00= (mat[0][0] * mat[0][0]+mat[0][1]*mat[1][0]) % m
        a01= (mat[0][0] * mat[0][1]+mat[0][1]  *mat[1][1]) % m
        a10= (mat[1][0] * mat[0][0]+mat[1][1]*  mat[1][0]) % m
        a= (mat[1][0] * mat[0][1]+mat[1][1]* mat[1][1]) % m
        mat= [[a00, a01],[a10, a]]

        x= x//2
    print(res[0][0],res[0][1])
    print(res[1][0],res[1][1])
