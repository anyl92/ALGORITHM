# import sys
# sys.stdin = open('findway_inp.txt', 'r')

nodeinfo = [[5,3],[11,5],[13,3],[3,5],[6,1],[1,3],[8,6],[7,2],[2,2]]

def sol(nodeinfo):
    ans = [[]]
    dep = {}
    tree = []

    for i, v in enumerate(nodeinfo):
        if v[1] in dep:
            dep[v[1]] += [(v[0], i+1)]
        else:
            dep[v[1]] = [(v[0], i+1)]
    print(dep)

    keys = sorted(list(dep.keys()))
    print(keys)

    for key in keys:
        cur = dep.get(key)
        tree.append(cur[1])


    return ans

sol(nodeinfo)

