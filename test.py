N = 4
V = [0] * N
T = [i for i in range(N)]

count = 0
def perm(k):
    global count
    if k == N:
        print(T)
        count += 1
        return
    for i in range(k, N):
        T[k], T[i] = T[i], T[k]
        V[i] = 1
        perm(k + 1)
        T[k], T[i] = T[i], T[k]
        V[i] = 0


perm(0)
print(count)