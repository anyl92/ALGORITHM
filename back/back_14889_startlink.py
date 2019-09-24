import sys
sys.stdin = open('input.txt', 'r')

T = int(input())
L = [list(map(int, input().split())) for _ in range(T)]
print(L)