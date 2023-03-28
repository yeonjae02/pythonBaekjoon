n = int(input())
for i in range(n):
    cnt = 0
    check = 1
    s = input()
    for j in range(0, len(s)):
        if s[j] == '(':
            cnt += 1
        else:
            if cnt < 1:
                check = 0
            else:
                cnt -= 1
    if cnt == 0 and check == 1:
        print("YES")
    else:
        print("NO")