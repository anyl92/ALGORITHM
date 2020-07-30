import sys
sys.stdin = open('9625.txt', 'r')

K = int(input())
a, b = 1, 0
fibo = [0 for _ in range(K+1)]


def top_down_fibo(n):
    if fibo[n] > 0:
        return fibo[n]

    if n <= 1:
        fibo[n] = n
        return fibo[n]

    else:
        fibo[n] = top_down_fibo(n-1) + top_down_fibo(n-2)
        return fibo[n]


if K == 0:
    print(a, b)
elif K == 1:
    a -= 1
    b += 1
    print(a, b)
else:
    top_down_fibo(K)
    print(fibo[-2], fibo[-1])
