import sys
sys.stdin = open('input.txt', 'r')
# 142
a = int(input())
i = 1
while True:
    print('*'*i)
    i += 1
    if i == a:
        while i != 0:
            print('*'*i)
            i -= 1
        break