import sys
sys.stdin = open('2529.txt', 'r')

K = int(input()) + 1
L = input().split()

N = 10
a = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
t = [0] * K
V = [0] * N

chk = 0
min_ans = ''
max_ans = ''


def perm(k):
    global chk, min_ans, max_ans
    if k == K:
        for x in range(K - 1):
            if L[x] == '<':
                if not t[x] < t[x + 1]:
                    break
            elif L[x] == '>':
                if not t[x] > t[x + 1]:
                    break
        else:
            if not chk:
                for e in t:
                    min_ans += str(e)
                chk = 1
            max_ans = ''
            for e in t:
                max_ans += str(e)
    else:
        for i in range(N):
            if not V[i]:
                t[k] = i
                V[i] = 1
                perm(k + 1)
                V[i] = 0


perm(0)

print(max_ans)
print(min_ans)