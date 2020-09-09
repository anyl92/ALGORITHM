import sys
sys.stdin = open('16943.txt', 'r')


def perm(k):
    global res
    if k == R:
        if T[0] == 0:
            return
        tmp_str = ''
        for t in T:
            tmp_str += str(t)
        tmp_int = int(tmp_str)
        if tmp_int <= int(B):
            if res < tmp_int:
                res = tmp_int
    else:
        for i, v in enumerate(A):
            if V[i]:
                continue
            T[k] = int(v)
            V[i] = 1
            perm(k + 1)
            V[i] = 0


A, B = map(str, input().split())
R = len(A)
T = [0 for _ in range(R)]
V = [0 for _ in range(R)]

res = -1
perm(0)
print(res)
