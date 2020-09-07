import sys
sys.stdin = open('15500.txt', 'r')

N = int(input())
cur, cnt = N, 0
one = list(map(int, input().split()))
two = []
res = []
ret = []

while one or two:
    for i, v in enumerate(one[::-1]):
        if v == cur:
            for j in range(i):
                two.append(one.pop())
                cnt += 1
                ret.append([1, 2])
            res.append(one.pop())
            cnt += 1
            ret.append([1, 3])
            cur -= 1
            break

    for i, v in enumerate(two[::-1]):
        if v == cur:
            for j in range(i):
                one.append(two.pop())
                cnt += 1
                ret.append([2, 1])
            res.append(two.pop())
            cnt += 1
            ret.append([2, 3])
            cur -= 1
            break

print(cnt)
for x in ret:
    print(x[0], x[1])
