import sys
import collections
sys.stdin = open('4949.txt', 'r')

while True:
    s = collections.deque([])
    inp = collections.deque(input())
    print(inp, 'inp')
    if inp[0] == '.':
        break

    while inp:
        cur = inp.popleft()
        if cur == '(' or cur == '[':
            s.append(cur)
        elif cur == ')':
            if s and s[-1] == '(':
                s.pop()
            else:
                print('no')
                break
        elif cur == ']':
            if s and s[-1] == '[':
                s.pop()
            else:
                print('no')
                break
    else:
        if not s:
            print('yes')
        else:
            print('no')
    print('------------------')