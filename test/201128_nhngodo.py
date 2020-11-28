# 1
class Solution:
    def solution(self, goods):

        # 두 명씩만 묶어 계산할 경우
        two = 999999999
        for i in range(3):
            idx = [0, 1, 2]
            idx.remove(i)
            tmp1 = goods[i]
            tmp2 = 0
            for x in idx:
                tmp2 += goods[x]
            if tmp1 >= 50:
                tmp1 -= 10
            if tmp2 >= 50:
                tmp2 -= 10
            two = min(two, tmp1 + tmp2)

        # 모두 한번에 계산할 경우
        three = sum(goods)
        if three >= 50:
            three -= 10

        # 각자 따로 계산할 경우
        one = 0
        for good in goods:
            if good >= 50:
                one += good - 10
            else:
                one += good

        # 모든 경우 중 최소 비용을 리턴합니다
        return min(one, two, three)


S = Solution()
S.solution([46,62,9])


# 2
class Solution:
    def solution(self, page, broken):
        total = [0] * 5000
        cnt_broken = [0] * 9
        for br in broken:
            cnt_broken[br-1] += 1
        print(cnt_broken)
        for i in range(1, len(total)):
            for j in str(i):
                j = int(j)
                if not cnt_broken[j-1]:
                    total[j-1] += 1
        print(total)
        return 0


S = Solution()
S.solution(5457, [6,7,8])


# 3
class Solution:
    def solution(self, s, n):
        counting_list = [0] * 26
        for st in s:
            counting_list[ord(st)-97] += 1

        max_cnt, min_cnt = 0, 9999
        for i, e in enumerate(counting_list):
            if e:
                if max_cnt < e:
                    max_cnt = e
                    max_idx = i
                if min_cnt > e:
                    min_cnt = e
                    min_idx = i

        flag = 0
        while True:
            if n == 0:
                break
            if counting_list[min_idx] == 0:
                flag = 1
            if counting_list[max_idx] == 0:
                break

            if flag:
                counting_list[max_idx] -= 1
            else:
                counting_list[min_idx] -= 1
            n -= 1

        return counting_list[max_idx] - counting_list[min_idx]


S = Solution()
S.solution("aaaaabbc", 1)


# # 4
# class Solution:
#     def solution(self, cardNumber):
#         cardNumberList = list(map(int, cardNumber))
#         lenString = len(cardNumber)
#         flag = 1 if lenString % 2 else 0  # len 홀1 짝0 판별
#
#         for i in range(lenString):
#             if flag:
#                 if i % 2:  # 홀수개수 짝수위치
#                     cardNumberList[i] *= 2
#             else:
#                 if not i % 2:  # 짝수개수 홀수위치
#                     cardNumberList[i] *= 2
#         print(cardNumberList)
#         ans = 0
#         for num in cardNumberList:
#             tmp = 0
#             while num > 10:
#                 tmp += num % 10
#                 num //= 10
#             ans += tmp
#             ans += num
#         print(ans, '답')
#         if ans == 0 or ans % 10:
#             return 'INVALID'
#         return 'VALID'
#
#
# S = Solution()
# print(S.solution("26227174957722514961366"))


# # 5
# class Solution:
#     def solution(self, votes):
#         target = votes.pop(0)
#         cnt = 0
#         votes.sort(reverse=True)
#         print(votes, target)
#         while votes and votes[0] >= target:
#             votes[0] -= 1
#             target += 1
#             cnt += 1
#             votes.sort(reverse=True)
#             print(votes, target)
#         return cnt
#
#
# S = Solution()
# print(S.solution([10,10,10,10]))