import sys
sys.stdin = open('15904.txt', 'r')

inp = list(input().replace(' ', ''))
print(inp)

answer = ['U', 'C', 'P', 'C']
result = []
i = 0
flag = 0
while answer != result:
    if not inp:
        flag = 0
        break

    ans = answer[i]
    cur = inp.pop(0)
    if ans == cur:
        i += 1
        result.append(cur)
        continue
else:
    flag = 1

if flag:
    print('I love UCPC')
else:
    print('I hate UCPC')