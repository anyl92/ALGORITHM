import itertools

perm = list(itertools.permutations([0, 1, 2, 3], 3))
print(perm)

repeat_perm = list(itertools.product([1, 2, 3], repeat=2))
print(repeat_perm)

comb = list(itertools.combinations([0, 1, 2, 3], 3))
print(comb)

repeat_comb = list(itertools.combinations_with_replacement([0, 1, 2, 3], 3))
print(repeat_comb)


s = [1, 2, 3, 6, 10, 15, 20, 22, 24]
r = [[]]
for e in s:
    r += [[e]+x for x in r]
print(r)


test = [1, 2, 1, 3, 2, 4, 2, 5, 4, 6, 5, 6, 6, 7, 3, 7]

nodelist1 = [[0]*8 for _ in range(8)]  # 행렬을 만들고
for i in range(len(test)//2):
    nodelist1[test[2*i]][test[2*i+1]] = 1  # 그 자리를 채워
    nodelist1[test[2*i+1]][test[2*i]] = 1  # 양방향

nodelist2 = [[] for _ in range(8)]  # 배열을 만들고
for i in range(len(test)//2):
    nodelist2[test[2*i]].append(test[2*i+1])  # 배열을 추가
    nodelist2[test[2*i+1]].append(test[2*i])  # 양방향
print(nodelist2)


key=lambda x:(x[0], -x[1])