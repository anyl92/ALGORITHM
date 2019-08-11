my = [9, 2, 3, 4, 5, 6]

real = [1, 2, 3, 4, 5, 6]
bonus = 8

# [1, 2, 3] => list / {1, 2, 3} => set / (1, 2, 3) => tuple / {'a': 'A'} => dict
match = set(my).intersection(set(real))
match_count = len(match)

if match_count == 6:
    result = '1등'
elif match_count == 5:
    if bonus in my:
        result = '2등'
    else:
        result = '3등'
elif match_count == 4:
    result = '4등'
elif match_count == 3:
    result = '5등'
else:
    result = '꽝ㅠ'

print(result)
