res = 2
pibo_list = [1, 2, 3]
n = 3

while n <= 4000000:
    n = pibo_list[-1] + pibo_list[-2]
    pibo_list.append(n)
    if n % 2 == 0:
        res += n

print(res)