import sys
sys.stdin = open('15663.txt', 'r')

N, M = list(map(int, input().split()))
perm_list = sorted(list(map(int, input().split())))
