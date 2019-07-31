# codewars - Find the odd int

def find_it(seq):
    sseq = set(seq)
    count_i = 0
    for i in sseq:
        if i in seq:
            count_i = seq.count(i)
            if count_i % 2 :
                return i

print(find_it([20,1,-1,2,-2,3,3,5,5,1,2,4,20,4,-1,-2,5]))


import operator

def find_it(xs):
    return reduce(operator.xor, xs)