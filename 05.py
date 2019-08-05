# codewars - Find The Parity Outlier
"""
정수를 포함하는 배열 (적어도 3의 길이를 갖지만 크기는 매우 클
 수 있음)이 제공됩니다. 배열은 전적으로 홀수 인 정수로 구성되거
 나 단일 정수를 제외하고는 모두 짝수 정수로 구성 N됩니다. 배열을 
 인수로 취하여이 "이상 값"을 반환하는 메서드를 작성합니다 N.

 [2, 4, 0, 100, 4, 11, 2602, 36]
Should return: 11 (the only odd number)

[160, 3, 1719, 19, 11, 13, -21]
Should return: 160 (the only even number)
"""

def find_outlier(integers):
    odd = even = 0
    for i in integers:
        if i % 2 :
            odd += 1
            if odd == 1:
                tem_odd = i
        else:
            even += 1
            if even == 1:
                tem_even = i

        if even > 1 and odd == 1:
            return tem_odd
            break
        if odd > 1 and even == 1:
            return tem_even
            break

print(find_outlier([2, 4, 6, 8, 10, 3]))


def find_outlier(int):
    odds = [x for x in int if x%2!=0]
    evens= [x for x in int if x%2==0]
    return odds[0] if len(odds)<len(evens) else evens[0]


