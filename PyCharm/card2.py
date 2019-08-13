import sys
sys.stdin = open('card_input.txt', 'r')

def Card(N, H):
    number = {}
    for i in range(N):
        number[H[i]] = H.count(str(i))
    print(number)

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    H = list(map(str, input().split()))
    res = Card(N, H)
    print('#%d %d %d' % (tc, res[0], res[1]))