import sys
sys.stdin = open('11655.txt', 'r')

inp = input()
res = ''

for i, v in enumerate(inp):
    cur = ord(v)
    if 65 <= cur <= 90:  # 대문자
        cur += 13
        if cur > 90:
            cur = 65 + (cur - 91)
        res += chr(cur)
    elif 97 <= cur <= 122:  # 소문자
        cur += 13
        if cur > 122:
            cur = 97 + (cur - 123)
        res += chr(cur)
    else:
        res += v

print(res)
