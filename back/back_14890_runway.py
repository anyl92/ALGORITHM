import sys
sys.stdin = open('14890.txt', 'r')

N, K = map(int, input().split())
L = [list(map(int, input().split())) for _ in range(N)]

cnt = 0

for i in range(N):
    tmp = L[i][0]
    for j in range(1, N):
        if tmp != L[i][j]:
            break
    else:
        cnt += 1

for i in range(N):
    tmp = L[0][i]
    for j in range(1, N):
        if tmp != L[j][i]:
            break
    else:
        cnt += 1



for i in range(N):
    for j in range(1, N):  # 시작값이 있으므로 1 idx 부터
        tmp_list = []  # 값을 바꿀 임시 배열
        pre = L[i][j - 1]
        cur = L[i][j]
        if pre - cur == 1 and j+K <= N and L[i][j+1] != 11:  # 왼쪽이 한 칸 더 높고 11 아니면
            tmp_list += [(i, j)]
            for k in range(1, K):  # 설치 길이만큼
                if L[i][j+1] != L[i][j+k+1] and L[i][j+k+1] != 11:  # 그 장소들의 높이가 다르면 안됨 11도 안됨
                    break
                tmp_list += [(i, j+k+1)]  # 같으면 배열에 저장
            else:  # 다르지 않았다면
                for i, j in tmp_list:  # 좌표를 뽑아냄
                    L[i][j] = 11  # 설치 값 추가
        elif pre - cur == -1 and j+K >= 0 and L[i][j] != 11:  # 오른쪽
            tmp_list += [(i, j)]
            for k in range(1, K):
                if L[i][j] != L[i][j-k] and L[i][j-k] != 11:
                    break
                tmp_list += [(i, j-k)]
            else:
                for i, j in tmp_list:
                    L[i][j] == 11


for a in L:
    print(a)

