import sys
sys.stdin = open('2110.txt', 'r')

home, wifi = map(int, input().split())
L = [int(input()) for _ in range(home)]
print(home, wifi, L)

