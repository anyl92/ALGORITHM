import sys
sys.stdin = open('16120.txt', 'r')

inps = list(input())
stack = []
cnt = 0

for inp in inps:
    if cnt > 2:
        if inp == 'P' and stack[cnt-1] == 'A' and stack[cnt-2] == 'P' and stack[cnt-3] == 'P':
            stack.pop()
            stack.pop()
            cnt -= 2
            continue
    stack.append(inp)
    cnt += 1

if len(stack) == 1 and stack[0] == 'P':
    print('PPAP')
else:
    print('NP')
