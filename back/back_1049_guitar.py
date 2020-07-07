import sys
sys.stdin = open('1049.txt', 'r')

N, M = map(int, input().split())
brand_list = [list(map(int, input().split())) for _ in range(M)]

single_benefit = 9999999
bundle_benefit = 9999999

for brand in brand_list:
    if brand[1] < single_benefit:  # 낱개 중 가장 저렴이 찾기
        single_benefit = brand[1]
    if brand[0] < bundle_benefit:  # 묶음 중 가장 저렴이 찾기
        bundle_benefit = brand[0]

single_calc = N * single_benefit  # 모두 낱개 구매
if N % 6 == 0:
    bundle_calc = N // 6 * bundle_benefit  # 모두 묶음 구매
else:
    bundle_calc = ((N // 6) + 1) * bundle_benefit  # 묶음 구매 후 낱개가 남는 구매
shuffle_calc = ((N // 6) * bundle_benefit) + ((N % 6) * single_benefit)  # 묶음 + 낱개 구매

calc_list = [single_calc, bundle_calc, shuffle_calc]
print(min(calc_list))
