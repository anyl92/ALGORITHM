import sys
sys.stdin = open('input.txt', 'r')

a = int(input())

def square(n):
    k = 1
    for i in range(n):
        for j in range(n):
            print(k, end=' ')
            k += 1
        print()

square(a)