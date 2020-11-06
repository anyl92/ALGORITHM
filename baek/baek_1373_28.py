import sys
import collections

sys.stdin = open('1373.txt', 'r')
inp = collections.deque(list(sys.stdin.readline().strip()))

r = collections.deque([])
i, n = 0, 0

while inp:
    tmp = int(inp.pop())

    if tmp:
        n += 2 ** i
    i += 1

    if i == 3 or not inp:
        r.insert(0, str(n))
        i, n = 0, 0

# while r != ['0'] and r[0] == '0':
while len(r) > 1 and r[0] == '0':
    r.popleft()
for rr in r:
    print(rr, end='')
