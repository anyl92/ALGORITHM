import sys
sys.stdin = open('5557.txt', 'r')

N = int(input())
L = list(map(int, input().split()))

answer = L.pop()
print(answer)
print(L)
cnt = 0

def sol(i, res):
    global cnt

    addtmp = res + L[i]
    subtmp = res - L[i]
    if addtmp > 20:
        return
    if subtmp < 0:
        return
    if addtmp == answer or subtmp == answer:
        cnt += 1
        return

    sol(i, answer + L[i])
    sol(i, answer - L[i])


result = 0
for idx in range(len(L)-1):
    sol(idx, result)


print(cnt)