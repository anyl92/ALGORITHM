import sys
sys.stdin = open('input.txt')

for tc in range(1, 11):
    N = int(input())
    L = [list(input()) for _ in range(100)]

    comp = []
    for row in range(len(L)):
        for i in range(len(L)):
            for j in range(len(L), -1, -1):
                row_list = L[row][i:j]
                if row_list == row_list[::-1]:
                    if len(row_list) > len(comp):
                        comp = row_list

    for k in range(len(L)):
        col_list = []
        for col in range(len(L)):
            col_list += L[col][k]
        for i in range(len(L)):
            for j in range(len(L), -1, -1):
                col_list2 = col_list[i:j]
                if col_list2 == col_list2[::-1]:
                    if len(col_list2) > len(comp):
                        comp = col_list2
    print(len(comp))