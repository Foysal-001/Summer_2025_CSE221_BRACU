

#wrong answer on test 10
'''def helper(a):
    for i in range(len(a)-1):
        if a[i] > a[i+1]:
            return False    
        return True
n=int(input())
s=list(map(int, input().split()))
if n==1:
    print('YES')
elif n==2:
    if s[0] <= s[1]:
        print('YES')
else:
    count=0
    if len(set(s)) == n:
        for i in range(n):
            for j in range(i + 1, n):
                if s[i] > s[j]:
                    count += 1
        print("YES" if count % 2 == 0 else "NO")
    else:
        for k in range(n):
            for i in range(n-2):
                if s[i]>s[i+1] or s[i]> s[i+2]:
                    s[i:i+3]= s[i:i+3][::-1]
        if helper(s):
            print('YES')
        else:
            print('NO')'''
                
def helper(s):
    new_lst = s.copy()
    for i in range(len(new_lst)):
        for j in range(i + 1, len(new_lst)):
            if new_lst[j] < new_lst[i]:
                new_lst[i], new_lst[j] = new_lst[j], new_lst[i]
    return new_lst
        

N = int(input())
s = list(map(int, input().split()))
even = []
odd = []
for i in range(N):
    if i % 2 == 0:
        even.append(s[i])
    else:
        odd.append(s[i])
sort_s = sorted(s)
evensort = []
oddsort = []
for i in range(N):
    if i % 2 == 0:
        evensort.append(sort_s[i])
    else:
        oddsort.append(sort_s[i])
if helper(even) == helper(evensort) and helper(odd) == helper(oddsort):
    print("YES")
else:
    print("NO")

