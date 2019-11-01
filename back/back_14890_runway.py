import sys
sys.stdin = open('14890.txt', 'r')

N, K = map(int, input().split())
L = [list(map(int, input().split())) for _ in range(N)]

# for i in range(N):
#     for j in range(N):
#         CL[i][j] = L[i][j]

SL = [[0]*N for _ in range(N)]
for i in range(N):
    for j in range(N):
        SL[j][i] = L[i][j]

cnt = 0


def find(L):
    global cnt

    for i in range(N):
        flag = False
        chk, tmp = 0, 0
        while not tmp:
            if CL[i][chk] != 11:
                tmp = L[i][chk]
                break
            else:
                chk += 1

        j = chk+1
        while j < N:
            if CL[i][j] == 11:
                ele_cnt = 0
                tmp_left = L[i][j-1]
                while CL[i][j] == 11:
                    ele_cnt += 1
                    j += 1
                    if j > N-1:
                        flag = True
                        print(L[i], 'flag')
                        cnt += 1
                        break
                if flag:
                    continue
                tmp_right = L[i][j]
                calc = abs(tmp_left-tmp_right)
                if calc == 0:
                    break
                if (ele_cnt//K) == calc:
                    tmp = L[i][j]
                    j += 1
                    continue
            if L[i][j] != tmp:
                j += 1
                break
            j += 1
        else:
            if not flag:
                print(L[i], 'cnt')
                cnt += 1

    return cnt

    # for i in range(N):
    #     tmp = L[i][0]
    #     for j in range(1, N):
    #         if tmp != L[i][j]:
    #             break
    #     else:
    #         cnt += 1
    #
    # for i in range(N):
    #     tmp = L[0][i]
    #     for j in range(1, N):
    #         if tmp != L[j][i]:
    #             break
    #     else:
    #         cnt += 1


def runway(L):
    for i in range(N):
        for j in range(1, N):
            tmp_list = []
            left = L[i][j - 1]
            right = L[i][j]

            if left - right == 1 and j+K <= N :  # 왼쪽이 한 칸 더 높
                tmp_list += [(i, j)]
                for k in range(1, K):  # 설치 길이만큼
                    if right != L[i][j+k] or CL[i][j+k] == 11 or CL[i][j] == 11:
                        tmp_list = []
                        break
                    tmp_list += [(i, j+k)]  # 같으면 배열에 저장
                if tmp_list:
                    for i, j in tmp_list:  # 좌표를 뽑아냄
                        CL[i][j] = 11  # 설치 값 추가

            elif left - right == -1 and j-K >= 0:  # 오른쪽이 한 칸 더 높
                tmp_list += [(i, j-1)]
                for k in range(1, K):
                    if left != L[i][j-k-1] or CL[i][j-k-1] == 11 or CL[i][j-1] == 11:
                        tmp_list = []
                        break
                    tmp_list += [(i, j-k-1)]
                if tmp_list:
                    for i, j in tmp_list:  # 좌표를 뽑아냄
                        CL[i][j] = 11  # 설치 값 추가

    for a in CL:
        print(a)

    find(L)



for l in (L, SL):
    CL = [[0] * N for _ in range(N)]
    runway(l)

print(cnt)