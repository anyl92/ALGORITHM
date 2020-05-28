def sol():
    max_val = 0
    for n1 in range(999, 900, -1):
        n2 = 999
        while n2 > 900:
            ans = n1 * n2
            str_ans = str(ans)
            if str_ans[::-1] == str_ans:
                if max_val < ans:
                    max_val = ans
            n2 -= 1
    return max_val

print(sol())