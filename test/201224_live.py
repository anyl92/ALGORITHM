# inp = [1, 2, ..]

total = 0
for i in range(1, 101):
    total += i

for i in inp:
    total -= i

print(total)


# -------------



inp = 'madam'
leng = len(inp)
j = leng-1
# for i, v in enumerate(inp):
for i in range(leng//2):
    if inp[i] == inp[j-i]:
        continue
    else:
        break
    j -= 1
else:
    print('pel')


