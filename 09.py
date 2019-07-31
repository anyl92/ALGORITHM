# codewars - Sum of Digits / Digital Root
# digital_root(942)
# => 9 + 4 + 2
# => 15 ...
# => 1 + 5
# => 6

def digital_root(n):
    numrange = len(str(n))
    if not n:
        return 0
    while numrange > 1:
        sumlist = 0
        for i in range(0, numrange):
            i = str(n)[i]
            sumlist += int(i)
        if len(str(sumlist)) == 1:
            return sumlist
        else:
            numrange = sumlist
            return digital_root(numrange)

print(digital_root(0))


def digital_root(n):
    return n if n < 10 else digital_root(sum(map(int,str(n))))

def digital_root(n):
    return n%9 or n and 9 
