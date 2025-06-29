for i in range(int(input())):
    n=int(input())
    a=list(map(int, input().split()))
    flag = True
    for j in range(n-1):
        if a[j] <= a[j+1]:
            continue
        else:
            flag = False
        
    print('YES' if flag == True else 'NO')