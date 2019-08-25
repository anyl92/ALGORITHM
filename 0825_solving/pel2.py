import sys
sys.stdin = open('input.txt')

for tc in range(1, 11):
    N = int(input())
    L = [list(input()) for _ in range(100)]
    print(L[0])
    count = 0
    count2 = 0
    n = 3
    i = 0
    j = 0
    f = 0
    comp_str = ''
    while i < 100:
        while j < 100-n+1:
        #for j in range(100-n+1):
            comp = L[i][j:j+n]
            if comp == comp[::-1]:
                print('pel', comp)
                count = len(comp)
                n += 1
                j = 0
                f = 1
                break
            j += 1
            f = 0
        if f == 1:
            continue
        else:
            i += 1

    # for i in range(100-n+1):
    #     for j in range(100):
    #         for k in range(n):
    #             comp_str += L[i+k][j]
    #             print(comp_str)
    #         if comp_str == comp_str[::-1]:
    #             print('pel', comp_str)
    #             count = len(comp_str)
    #     n += 1
    #
        #     if comp_str == comp_str[::-1]:
        #         print('pel', comp_str)
        #         count2 = len(comp_str)
        #         comp_str = ''
        #         break
        #     comp_str = ''
        # n += 1
    # if count > count2:
    #     print(count)
    # else:
    #     print(count2)