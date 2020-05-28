def squsum():
    res = 1
    for i in range(2, 101):
        res += i*i
    return res

def sumsqu():
    res = 1
    for i in range(2, 101):
        res += i
    return res*res

print(sumsqu() - squsum())