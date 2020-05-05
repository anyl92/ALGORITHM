# 1
def solution(inputString):
    answer = 0
    stack = [[], [], [], []]
    openbre = ['(', '{', '[', '<']
    closebre = [')', '}', ']', '>']

    for word in inputString:
        if word == '(':
            stack[0].append(word)
        elif word == '{':
            stack[1].append(word)
        elif word == '[':
            stack[2].append(word)
        elif word == '<':
            stack[3].append(word)

        elif word in closebre:
            if word == closebre[0]:
                k = 0
            elif word == closebre[1]:
                k = 1
            elif word == closebre[2]:
                k = 2
            elif word == closebre[3]:
                k = 3

            if stack[k] and stack[k][0] == openbre[k]:
                answer += 1
                stack.pop()
            else:
                return -1
    return answer


# print(solution('Hello, world!'))
# print(solution('line [plus]'))
# print(solution('if (Count of eggs is 4.) {Buy milk.}'))
# print(solution('>_<'))


# 2
def solution(answer_sheet, sheets):
    answer = 0
    for i in range(len(sheets)):
        for j in range(i+1, len(sheets)):
            doubt = 0
            chect = [0] * len(answer_sheet)
            for k in range(len(answer_sheet)):
                if sheets[i][k] == sheets[j][k]:
                    if sheets[i][k] != answer_sheet[k]:
                        doubt += 1
                        chect[k] = 1
            
            maxx, cnt = 0, 0
            for c in chect:
                if c: 
                    cnt += 1
                else:
                    if maxx <= cnt:
                        maxx = cnt
                        cnt = 0
            if maxx < cnt:
                maxx = cnt

            ans = doubt + (maxx*maxx)

            if answer < ans:
                answer = ans
    return answer


# print(solution("4132315142", ["3241523133","4121314445","3243523133","4433325251","2412313253"]))
# print(solution("53241", ["53241", "42133", "53241", "14354"]))
# print(solution("24551", ["24553", "24553", "24553", "24553"]))


# 3
maxx = 0
def solution(road, n):
    repair = []
    for i, r in enumerate(road):
        if r == '0':
            repair.append(i)
    
    if len(repair) <= n:
        return len(road)
    
    choiced = [0]*n
    def comb(k, s, road):
        global maxx
        if (k == n):
            for choice in choiced:
                road[choice] = '1'

            cnt, cntmax = 0, 0
            for r in road:
                if r == '1':
                    cnt += 1
                else:
                    if cntmax < cnt:
                        cntmax = cnt
                        cnt = 0

            if maxx < cntmax:
                maxx = cntmax

            for choice in choiced:
                road[choice] = '0'
            
        else:
            for i in range(s, len(repair) + (k - n) + 1):
                choiced[k] = repair[i]
                comb(k+1, i+1, road)

    comb(0, 0, list(road))
    return maxx


# print(solution("111011110011111011111100011111", 3))
# print(solution("001100", 5))


# 4
def solution(snapshots, transactions):
    answer = [[]]
    info = {}
    transactions = sorted(transactions, key=lambda x:x[0])

    num = 1
    for t in transactions:
        if int(t[0]) < num:
            continue

        if info.get(t[2]):
            if t[1] == 'SAVE':
                res = int(snapshots[info.get(t[2])][1]) + int(t[3])
                snapshots[info.get(t[2])][1] = str(res)
            else:
                res = int(snapshots[info.get(t[2])][1]) - int(t[3])
                snapshots[info.get(t[2])][1] = str(res)

        else:
            for i, s in enumerate(snapshots):
                if s[0] == t[2]:
                    info[t[2]] = i
                    if t[1] == 'SAVE':
                        res = int(snapshots[i][1]) + int(t[3])
                        snapshots[i][1] = str(res)
                    else:
                        res = int(snapshots[i][1]) - int(t[3])
                        snapshots[i][1] = str(res)
                    break
            else:
                snapshots.append([t[2], '0'])
                i = len(snapshots)-1
                info[t[2]] = i
                if t[1] == 'SAVE':
                    res = int(snapshots[i][1]) + int(t[3])
                    snapshots[i][1] = str(res)
                else:
                    res = int(snapshots[i][1]) - int(t[3])
                    snapshots[i][1] = str(res)
        num += 1
    return snapshots


print(solution([
  ["ACCOUNT1", "100"], 
  ["ACCOUNT2", "150"]
],
[
  ["1", "SAVE", "ACCOUNT2", "100"],
  ["2", "WITHDRAW", "ACCOUNT1", "50"], 
  ["1", "SAVE", "ACCOUNT2", "100"], 
  ["4", "SAVE", "ACCOUNT3", "500"], 
  ["3", "WITHDRAW", "ACCOUNT2", "30"]
]))