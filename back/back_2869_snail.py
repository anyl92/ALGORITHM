import sys
sys.stdin = open('2869.txt', 'r')

A, B, V = list(map(int, input().split()))
n = ( V - B - 1 ) // (A - B) + 1
print(n)