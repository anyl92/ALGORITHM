def combinations(n, list, combos=[]):
    if combos is None:
        combos = []

    if len(list) == n:
        if combos.count(list) == 0:
            combos.append(list)
            combos.sort()
        return combos
    else:
        for i in range(len(list)):
            refined_list = list[:i] + list[i+1:]
            combos = combinations(n, refined_list, combos)
        return combos

li = [1, 2, 3, 4]
print(combinations(2, li))
