import sys
sys.stdin = open('input.txt', 'r')

a = list(map(int,input().split()))

minl = [-1]*len(a)
maxl = [-1]*len(a)
n = 0
m = 0
for i in range(len(a)):
    if a[i] >= 100:
        minl[n] = a[i]
        n+=1
    else:
        maxl[m] = a[i]
        m+=1
print(minl, maxl)

for i in range(10):
    if minl[i] < 100:
        break
    elif minl[i] < minl[i+1]:
        n = minl[i]

for i in range(10):
    if maxl[i] < 0:
        break
    elif maxl[i] > maxl[i+1]:
        m = maxl[i]
print(n, m)