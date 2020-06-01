for a in range(333):
    for b in range(a+1, 500):
        c = 1000 - a - b
        tmp = a*a + b*b
        if tmp > c*c:
            continue
        if tmp == c*c:
            print(a*b*c)