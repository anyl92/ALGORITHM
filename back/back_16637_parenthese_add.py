import sys
sys.stdin = open('16637.txt', 'r')


def calc(L):
    num_s = []
    opr_s = []
    for j in range(len(L)):
        if not L[j] == '':
            if type(L[j]) == str:
                opr_s += [L[j]]
            else:
                num_s += [L[j]]

    res = 0
    for k in range(len(opr_s)):
        num1 = num_s[k]
        num2 = num_s[k + 1]
        if opr_s[k] == '+':
            res = num1 + num2
        elif opr_s[k] == '-':
            res = (num1 - num2)
        elif opr_s[k] == '*':
            res = (num1 * num2)
        num_s[k+1] = res
    return res


def comp(tmp):
    global ans
    if ans < tmp:
        ans = tmp


def recur(i):
    if i + 3 > N:
        return

    while i < len(L) - 2:
        if L[i + 1] == '+':
            L[i + 2] = L[i] + L[i + 2]
        elif L[i + 1] == '-':
            L[i + 2] = L[i] - L[i + 2]
        elif L[i + 1] == '*':
            L[i + 2] = L[i] * L[i + 2]
        L[i], L[i + 1] = '', ''

        recur(i+4)
        comp(calc(L))
        L[i], L[i + 1], L[i + 2] = CL[i], CL[i + 1], CL[i + 2]

        i += 2


N = int(input())
L = list(input())

for i in range(len(L)):
    if i % 2 == 0:
        L[i] = int(L[i])

CL = []
for i in L:
    CL += [i]

if N == 1:
    print(L[0])
else:
    if N > 3:
        ans = calc(L)
        recur(0)
    else:
        ans = calc(L)
    print(ans)