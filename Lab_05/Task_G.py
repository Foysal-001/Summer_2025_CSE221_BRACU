import sys
from collections import deque
input=sys.stdin.readline
r,h=map(int,input().split())
mat=[list(input().strip()) for _ in range(r)]
ll=[[0]*h for _ in range(r)]
count=0
for i in range(r):
    for j in range(h):
        if mat[i][j]!='#' and not ll[i][j]:
            q=deque([(i,j)])
            ll[i][j]=1
            count2=0
            while q:
                x,y=q.popleft()
                if mat[x][y]=='D':
                    count2+=1
                if x+1<r and mat[x+1][y]!='#' and not ll[x+1][y]:
                    ll[x+1][y]=1
                    q.append((x+1,y))
                if x-1>=0 and mat[x-1][y]!='#' and not ll[x-1][y]:
                    ll[x-1][y]=1
                    q.append((x-1,y))
                if y+1<h and mat[x][y+1]!='#' and not ll[x][y+1]:
                    ll[x][y+1]=1
                    q.append((x,y+1))
                if y-1>=0 and mat[x][y-1]!='#' and not ll[x][y-1]:
                    ll[x][y-1]=1
                    q.append((x,y-1))
            count=max(count,count2)
print(count)
