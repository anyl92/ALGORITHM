# #1
# def solution(goods, coupons):
#     goods_list = []
#     for good in goods:
#         for g in range(good[1]):
#             goods_list.append(good[0])
#     goods_list.sort(reverse=True)
#
#     coupons_list = []
#     for coupon in coupons:
#         for c in range(coupon[1]):
#             coupons_list.append(coupon[0])
#     coupons_list.sort(reverse=True)
#     coupons_list = coupons_list[:len(goods_list)]
#
#     if len(coupons_list) < len(goods_list):
#         while len(coupons_list) != len(goods_list):
#             coupons_list.append(1)
#
#     for i in range(len(coupons_list)):
#         if coupons_list[i] != 1:
#             coupons_list[i] = (100 - coupons_list[i]) / 100
#
#     result_list = []
#     for j in range(len(coupons_list)):
#         tmp = goods_list[j] * coupons_list[j]
#         result_list.append(tmp)
#
#     result = 0
#     for r in result_list:
#         result += r
#
#     return result


# #2
# cnt = 0
# def solution(arr, k, t):
#     def comb(w, s, summ):
#         global cnt
#         if summ > t:
#             return
#
#         if w >= k:
#             if summ <= t:
#                 cnt += 1
#         for i in range(s, len(arr)):
#             comb(w + 1, i + 1, summ + arr[i])
#
#     comb(0, 0, 0)
#     return cnt

