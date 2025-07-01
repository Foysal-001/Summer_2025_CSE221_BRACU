n = int(input())
s = list(map(int, input().split()))
while True:
    flag = False
    for i in range(n-1):
       a= s[i] % 2      
       b = s[i+1] % 2
       if a == b:
          if s[i] > s[i+1]:
             temp = s[i]
             s[i] = s[i+1]
             s[i+1] = temp
             flag = True
    if flag == False:
        break
print(*s)
