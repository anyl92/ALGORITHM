import sys
sys.stdin = open('1476.txt', 'r')

find = list(map(int, input().split()))

year = 1
chk = [1, 1, 1]
while chk != find:
    for planet in range(3):
        chk[planet] += 1
    
    if chk[0] > 15:
        chk[0] = 1
    if chk[1] > 28:
        chk[1] = 1
    if chk[2] > 19:
        chk[2] = 1
    
    year += 1

print(year)