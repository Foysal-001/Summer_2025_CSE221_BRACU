import sys
input=sys.stdin.readline
n=int(input())
mat=[[0]*n for _ in range(n)]
for node in range(n):
    data=list(map(int, input().split()))
    count=data[0]
    if count:
        for dest in data[1:]:
            mat[node][dest]=1
for row in mat:
    print(*row)
