import sys
sys.stdin = open('2457.txt', 'r')

N = int(input())
L = [list(map(int, input().split())) for _ in range(N)]
print(N, L)

