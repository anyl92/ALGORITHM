import sys
sys.stdin = open('input.txt', 'r')

def perm(k):
    if k == M:  # k가 M과 같다는건 T배열이 다 채워졌다는 것
        for i in range(M):  # M만큼 돌며 T를 출력할것
            print(T[i], end=' ')
        print()
        return  # 리턴함으로써 다음 재귀 단계를 계속한다

    for i in range(1, N+1):  # i를 1부터 N+1 까지 [1, 2, 3, 4] 를 찾기위해
        if visited[i]:  # visited에 체크되어있다면
            continue  # 다음 수를 체크한다
        visited[i] = 1  # 확인할 것이므로 visited에 체크
        T[k] = i  # T배열의 k자리에 i를 추가
        perm(k+1)  # 다음 k자리의 수를 찾기 위하여
        visited[i] = 0  # 찾은뒤에는 0으로 바꿔주어 다음에 찾게 한다

N, M = map(int, input().split())
visited = [0] * (N+1)  # 방문한 인덱스 체크할 배열
T = [0] * M  # 출력할 순열 저장할 배열
perm(0)  # T배열의 k인덱스 0부터 순열찾기 시작