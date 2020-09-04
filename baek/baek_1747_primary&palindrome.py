def primary(n):
    for i in range(2, n):
        if n % i != 0:
            continue
        return False
    return True


def palindrome(n):
    if n[::-1] != n:
        return False
    return True


num = int(input())
while True:
    if num == 1:
        print(2)
        break
    if palindrome(str(num)) and primary(num):
        print(num)
        break
    num += 1
