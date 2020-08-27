import sys
sys.stdin = open('meetingroom_input.txt', 'r')

def func(k, cnt):
    while k < len(conf) - 1:
        for i in range(k + 1, len(conf)):
            if conf[k][1] <= conf[i][0]:
                cnt += 1
                k = i
                break
        else:
            return cnt
    return cnt

N = int(input())
conf = [list(map(int, input().split())) for _ in range(N)]

conf.sort(key=lambda x: (x[1], x[0]))
print(func(0, 1))
