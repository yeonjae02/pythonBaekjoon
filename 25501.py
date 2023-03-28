def recursion(s, l, r):
    if l >= r: return 1
    elif s[l] != s[r]: return 0
    else:
        global cnt
        cnt += 1
        return recursion(s, l+1, r-1)

def isPalindrome(s):
    return recursion(s, 0, len(s)-1)

n = int(input())
for i in range(n):
    cnt = 1
    string = input()
    print(isPalindrome(string), end=" ")
    print(cnt)