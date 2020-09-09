import sys
sys.stdin = open('1759.txt', 'r')

R, N = map(int, input().split())
L = sorted(list(map(str, input().split())))


def comb(k, s):
    consonant, vowel = 0, 0
    res = ''
    if k == R:
        for x in t:
            if x == 'a' or x == 'e' or x == 'i' or x == 'o' or x == 'u':
                vowel += 1
            else:
                consonant += 1
            res += x
        if vowel >= 1 and consonant >= 2:
            print(res)
    else:
        for i in range(s, N + (k - R) + 1):
            t[k] = L[i]
            comb(k + 1, i + 1)


t = [0] * R
comb(0, 0)
