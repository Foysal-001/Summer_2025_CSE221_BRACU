'''n = int(input())
t_name = []
d_time = []
lines = []  

for j in range(n):
    s = list(map(str, input().split()))
    t_name.append(s[0])
    d_time.append(s[6])
    lines.append(" ".join(s)) 

sort_n = t_name[:]
for i in range(n):
    for j in range(i + 1, n):
        if sort_n[i].lower() > sort_n[j].lower():
            sort_n[i], sort_n[j] = sort_n[j], sort_n[i]

count = [False] * n

for k in sort_n:
    train = []

    for i in range(n):
        if not count[i] and t_name[i].lower() == k.lower():
            h, m = map(int, d_time[i].split(":"))
            total_min = h * 60 + m
            train.append((total_min, i))  
    for i in range(len(train)):
        for j in range(i + 1, len(train)):
            if train[i][0] < train[j][0]:
                train[i], train[j] = train[j], train[i]

    for i , idx in train:
        print(lines[idx])
        count[idx] = True

n = int(input())
trains = []

for _ in range(n):
    line = input()
    parts = line.split()
    name = parts[0]
    time_str = parts[-1]
    hh, mm = map(int, time_str.split(':'))
    total_minutes = hh * 60 + mm
    trains.append((name, total_minutes, line))

keys = []
for train in trains:
    name_lower = train[0].lower()
    neg_time = -train[1]
    keys.append((name_lower, neg_time))

indices = list(range(n))
for i in range(n):
    for j in range(i+1, n):
        if keys[indices[i]] > keys[indices[j]]:
            indices[i], indices[j] = indices[j], indices[i]


for idx in indices:
    print(trains[idx][2])'''



#Submitted one 

N=int(input())
names=[]
times=[]
res=[]
pos=[]  
for i in range(N):
    line=input()
    parts=line.split()
    name=parts[0]
    t=parts[-1]
    h=int(t[:2])
    m=int(t[3:])
    total=h*60+m
    names.append(name)
    times.append(total)
    res.append(line)
    pos.append(i) 
for i in range(N):
    count=i
    for j in range(i+1, N):
        if names[j]<names[count]:
            count=j
        elif names[j] == names[count]:
            if times[j] > times[count]:
                count=j
            elif times[j] == times[count]:
                if pos[j] < pos[count]:
                    count=j
    if count != i:
        names[i],names[count]=names[count],names[i]
        times[i],times[count]=times[count],times[i]
        res[i],res[count]=res[count],res[i]
        pos[i],pos[count]=pos[count],pos[i]
for i in range(N):
    print(res[i])
