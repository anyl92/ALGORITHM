import sys
sys.stdin = open('6603.txt', 'r')

import itertools
while True:
    tc = list(map(int, input().split()))
    if tc == [0]:
        break
    k = tc.pop(0)
    result_list = sorted(list(itertools.combinations(tc, 6)))
    for result in result_list:
        for r in result:
            print(r, end=' ')
        print()
    print()