import sys
sys.stdin = open('input.txt')

def palin(list):
    i = 0
    fin = len(list) - 1
    stop = 0
    while fin != i and fin - i != 1:
        i += 1
        fin -= 1
        if list[i] != list[fin]:
            stop = 1
            break
    if stop == 1:
        return 0
    else:
        return len(list)


def palin_sero(list):
    i = 0
    fin = len(list) - 1
    while fin == i or fin - 1 == 1:
        i += 1
        fin -= 1
        if list[i] != list[fin]:
            break
    return len(list)


for _ in range(10):
    test_case = int(input())
    matrix = [[i for i in input()] for _ in range(100)]
    maxi = 3
    result = maxi + 1

    for i in range(100):
        for j in range(0, 99 - maxi):
            for k in range(j + maxi - 1, 100):
                if matrix[i][j] == matrix[i][k]:
                    if palin(matrix[i][j:k + 1]) > maxi:
                        maxi = palin(matrix[i][j:k + 1])
                        break
                    else:
                        continue
    for j in range(100):
        for i in range(0, 99 - maxi):
            test = []
            for k in range(i, 100):
                test.append(matrix[k][j])
                if matrix[i][j] == matrix[k][j]:
                    if palin(test) > maxi:
                        maxi = palin(test)
                        break
                else:
                    continue
    print('#{} {}'.format(test_case, maxi))