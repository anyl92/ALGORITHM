import sys
sys.stdin = open('10989.txt', 'r')

counting_list = [0 for _ in range(10001)]
N = int(sys.stdin.readline())
for n in range(N):
    counting_list[int(sys.stdin.readline())] += 1

for i, v in enumerate(counting_list):
    if v:
        sys.stdout.write((str(i) + '\n') * v)
