n = 20
while n:
    for mod_num in range(2, 21):
        if n % mod_num != 0:
            break
    else:
        print(n)
        break
    n += 1