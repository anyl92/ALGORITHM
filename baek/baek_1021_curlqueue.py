import sys
sys.stdin = open('1021.txt', 'r')

N, M = map(int, input().split())
q = [i for i in range(1, N+1)]
pop_list = list(map(int, input().split()))

res = 0
while pop_list:
    if q[0] == pop_list[0]:
        q.pop(0)
        pop_list.pop(0)
    else:
        cur = pop_list[0]
        right_idx = q.index(cur)
        left_idx = len(q) - right_idx

        if right_idx <= left_idx:
            for _ in range(right_idx):
                q.append(q.pop(0))
                res += 1
        else:
            for _ in range(left_idx):
                q.insert(0, q.pop())
                res += 1

print(res)