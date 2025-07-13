import sys
input = sys.stdin.readline

n = int(input())
a = list(map(int, input().split()))
m = int(input())
b = list(map(int, input().split()))

i = j = 0
merged = []
while True:
    if i == n and j == m:
        break
    if i == n:
        merged.append(b[j])
        j += 1
        continue
    if j == m:
        merged.append(a[i])
        i += 1
        continue
    if a[i] <= b[j]:
        merged.append(a[i])
        i += 1
    else:
        merged.append(b[j])
        j += 1

print(*merged)
