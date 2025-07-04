n=list(map(int, input().split()))
for i in range(len(n)):
    flag=False
    for j in range(len(n)- i- 1):
        if n[j] > n[j+1]:
            n[j+1],n[j] = n[j], n[j+1]
            flag=True
        else:
            continue

    
    if flag == False:
        print(n)
        break

    else:
        continue


#Best case time complexity O(N)
#worst case time complexity O(N^2)


    