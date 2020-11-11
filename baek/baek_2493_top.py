import sys
sys.stdin = open('2493.txt', 'r')

N = int(input())
L = list(map(int, input().split()))

s = []
for i, v in enumerate(L):
    if s:
        if s[-1][1] <= v:  # 직전 탑이 나보다 작거나 같을 때
            while s and s[-1][1] < v:  # 우선 작은 걸 다 빼
                s.pop()
            if not s:  # 그랬더니 아무것도 없다? 그러면 0 출력하고 넘어가기
                print(0, end=' ')
                s.append([i, v])
                continue
            if s[-1][1] == v:  # 작은걸 다 뺀 후 같은 높이다? 갈아치우기
                s.pop()
        print(s[-1][0]+1, end=' ')  # 직전 탑이 나보다 클 때
    else:
        print(0, end=' ')  # 보낼 탑이 없을 때
    s.append([i, v])

'6 4 5 2 5 1'
'''
처음에 6을 push, 4는 s[-1][0]확인 후 크니까 인덱스 출력 후 push
s = [[6, 1], [4, 2]] -> 5일때는 4가 작으니까 pop 후 6인덱스 출력 후 5push
s = [[6, 1], [5, 3]] => 2일때는 5인덱스 출력 후 2push
s = [[6, 1], [5, 3], [2, 4]] => 5임 2가 작으니까 pop후 5를 출력 후 같으니까 pop, 5push
s = [[6, 1], [5, 5]] => 1일때는 5인덱스 출력 후 1push
'''
'''
빈 스택에 순서대로 넣을거야
6이 들어감 s[-1]이없고 max가 없기 때문에 0
9가 들어감 s[-1]이작고 max도 6으로 작아서 0
5가 들어감 s[-1], max가 9이므로 9의 idx 2
7이 들어감 s[-1]는작고 max가 9이므로 9의 idx 2
4가 들어감 s[-1]가 크므로 7의 idx 4 
만약 이다음에
8이 들어오면 s[-1]는작고 max가9인데 9 idx까지 찾아가면서 큰거찾기
그럼 처음엔 s[-1]이 큰 걸 찾아야함
'''