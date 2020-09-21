import sys
sys.stdin = open('2812.txt', 'r')

N, K = map(int, input().split())
L = list(input())
counting_list = [0 for _ in range(10)]
for i in range(N-K):
    counting_list[int(L[i])] += 1

res_list = []
for count in range(len(counting_list)-1, -1, -1):
    if counting_list[count]:
        idx_list = list(filter(lambda x:L[x] == str(count), range(N-K-1)))

        for idx in idx_list:
            tmp_list = L[idx:idx+N]
            j = 1
            while len(tmp_list) != N-K:
                if tmp_list[i] < tmp_list[i+1]:
                    tmp_list.pop(i)
                else:
                    
                # tmp_list.pop(tmp_list.index(min(tmp_list)))
                j += 1
            res_list.append(int(''.join(tmp_list)))
            print(res_list)
print(max(res_list))