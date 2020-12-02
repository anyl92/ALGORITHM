# 3
def solution(bishops):
    answer = 64
    length = 0
    delta = [[1, 1], [-1, -1], [-1, 1], [1, -1]]
    board = [[0 for _ in range(8)] for _ in range(8)]
    for x, y in bishops:
        x = ord(x) - 65
        y = (8 - int(y)) * 1
        board[y][x] = 3
        length += 1

    for x, y in bishops:
        x = ord(x) - 65
        y = (8 - int(y)) * 1
        for dx, dy in delta:
            xx, yy = x + dx, y + dy
            while 0 <= xx < 8 and 0 <= yy < 8:
                if not board[yy][xx]:
                    board[yy][xx] = 1
                    answer -= 1
                xx += dx
                yy += dy
    return answer - length


bishops1 = ["D5"]
ret1 = solution(bishops1)

print("solution 함수의 반환 값은", ret1, "입니다.")

bishops2 = ["D5", "E8", "G2"]
ret2 = solution(bishops2)

print("solution 함수의 반환 값은", ret2, "입니다.")

# 4
def solution(s1, s2):
    answer = 0
    li_s1, li_s2 = list(s1), list(s2)
    len_s1, len_s2 = len(s1), len(s2)
    total = len_s1 + len_s2

    i = 0
    while i < min(len_s1, len_s2):
        # print(li_s1[len_s1-i-1:], li_s2[:i+1])
        if li_s1[len_s1 - i - 1:] == li_s2[:i + 1]:
            answer = max(answer, i + 1)
        i += 1

    j = 0
    while j < min(len_s1, len_s2):
        # print(li_s2[len_s2-j-1:], li_s1[:j+1])
        if li_s2[len_s2 - j - 1:] == li_s1[:j + 1]:
            answer = max(answer, j + 1)
        j += 1
    return total - answer


s1 = "ababc"
s2 = "abcdab"
ret = solution(s1, s2)

print("solution 함수의 반환 값은", ret, "입니다.")

# 5
def solution(phrases, second):
    length = len(phrases)
    downline = '_'*length
    total_string = downline + phrases
    i = second % length
    return total_string[i:i+14]


phrases = "happy-birthday"
second = 3
ret = solution(phrases, second)

print("solution 함수의 반환 값은", ret, "입니다.")

#