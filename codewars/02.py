# 10 이하의 모든 자연수를 3 또는 5의 배수로 나열하면 3, 5, 6 및 9가됩니다. 
# 이러한 배수의 합은 23입니다.
# 전달 된 숫자 아래 에 3 또는 5의 모든 배수의 합계를 반환하도록 솔루션을 마칩니다 .
# 참고 : 수의 배수 인 경우 모두 3, 5, 만 계산 한 번 .

def solution(number):
    sum_list = 0
    for i in range(0, number):
        if i % 3 == 0 or i % 5 == 0:
            sum_list += i
    return sum_list

print(solution(10))