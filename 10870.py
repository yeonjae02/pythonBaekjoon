fiboDic = {0:0, 1:1}

def fibo(n):
    if n not in fiboDic:
        fiboDic[n] = fibo(n-1)+fibo(n-2)
    return fiboDic[n]

n = int(input())
print(fibo(n))