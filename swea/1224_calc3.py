import sys
sys.stdin = open('calc_input.txt', 'r')

def postfix(N, L):
    op = ['(', '+', '*', '(']
    S = []
    R = []
    top = -1
    for i in L:
        if i == op[0]:
            S.append(i)
            top += 1
        elif i == ')':
            while S[top] != '(':
                R.append(S.pop())
                top -= 1
            S.pop()
            top -= 1
        elif i == '*':
            while S[top] == '*':
                R.append(S.pop())
                top -= 1
            S.append(i)
            top += 1
        elif i == '+':
            while S[top] == '*':
                R.append(S.pop())
                top -= 1
            S.append(i)
            top += 1
        else:
            R.append(i)
    return cal(R)

def cal(R):
    op = ['(', '+', '*', '(']
    S = []
    for i in range(len(R)):
        if R[i] in op:
            if R[i] == '+':
                num1, num2 = S.pop(), S.pop()
                S.append(num2+num1)
            elif R[i] == '*':
                num1, num2 = S.pop(), S.pop()
                S.append(num2*num1)
        else:
            S.append(int(R[i]))
    return S.pop()

for tc in range(1, 11):
    N = int(input())
    L = list(''.join(input()))
    res = postfix(N, L)
    print('#%d %d' % (tc, res))