# 1
def solution(code, day, data):
    pre_answer = []
    answer = []

    for d in data:
        cur = d.split()
        cur_price = int(cur[0][6:])
        cur_code = cur[1][5:]
        cur_day = cur[2][5:13]
        cur_sec = int(cur[2][5:])

        if code == cur_code and day == cur_day:
            pre_answer.append([cur_sec, cur_price])

    pre_answer.sort()
    for pre in pre_answer:
        answer.append(pre[1])

    return answer


# 2
def solution(board):
    delta = [[0, 1], [1, 1], [1, 0], [1, -1]]  # y,x

    def chk(j, i):
        for dy, dx in delta:
            x = i
            y = j
            dol = 0
            while dol < 5:
                xx = x + dx
                yy = y + dy
                if 0 <= xx < 15 and 0 <= yy < 15:
                    if board[yy][xx] != board[y][x]:
                        dol = 0
                        break
                else:
                    break

                dol += 1
                if dol == 4:
                    return board[yy][xx]
                y = yy
                x = xx

    for i in range(15):
        for j in range(15):
            if board[i][j] and chk(j, i):
                return chk(j, i)

    return 0


# 4
def solution(word, cards):
    answer = 0
    N = len(cards)

    k = 0
    while k < N:
        num_li = [i for i in range(N)]
        copy_word = []
        for w in word:
            copy_word.append(w)
        print(num_li, copy_word)

        y, x = 0, 0
        while num_li:
        #for x in num_li:
            for w in copy_word:
                if cards[y][x] == w:
                    num_li.remove(x)
                    copy_word.remove(w)
                    print(num_li, w, y, x ,'삭제')
                    y += 1
                    x += 1
                    continue
            else:
                break

        if num_li == []:
            answer += 1
        k += 1

    return answer


# 5
'''
SELECT   USERS.ID, 
    (CASE
     WHEN PAYS.AMOUNT IS NULL THEN 0
     ELSE SUM(PAYS.AMOUNT)
     END) AS TOTAL_PRICE
FROM     GAME_USERS USERS LEFT OUTER JOIN PAYMENTS PAYS
ON       USERS.ID = PAYS.USER_ID
GROUP BY USERS.ID
ORDER BY USERS.ID
'''