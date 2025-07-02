'''n=int(input())
id=list(map(int, input().split()))
mark=list(map(int, input().split()))
count=0
info=[]
for i in range(n):
    info.append((id[i], mark[i]))

for i in range(n):
    idx = i
    for j in range(i + 1, n):
        if info[j][1] > info[idx][1]:
            idx = j
        elif info[j][1] == info[idx][1] and info[j][0] < info[idx][0]:
            idx = j
    if idx != i:
        info[i], info[idx] = info[idx], info[i]
        count += 1

print(f'Minimum swaps: {count}')
for id, mark in info:
    print(f'ID: {id} Mark: {mark}')'''


n = int(input())
id = list(map(int, input().split()))
mark = list(map(int, input().split()))

count = 0

for i in range(n):
    idx = i
    for j in range(i + 1, n):
        if mark[j] > mark[idx]:
            idx = j
        elif mark[j] == mark[idx] and id[j] < id[idx]:
            idx = j
    if idx != i:
        id[i], id[idx] = id[idx], id[i]
        mark[i], mark[idx] = mark[idx], mark[i]
        count += 1

print(f'Minimum swaps: {count}')
for i in range(n):
    print(f'ID: {id[i]} Mark: {mark[i]}')

    
