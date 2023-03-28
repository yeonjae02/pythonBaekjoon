n = int(input())
result = 0
name = []

for i in range(n):
    s = input()
    name.append(s[::-1])

name.sort()

for i in range(n-1):
    cnt = 0
    while name[i][cnt] == name[i+1][cnt]:
        cnt += 1
    if result < cnt+1:
        result = cnt+1

print(result)