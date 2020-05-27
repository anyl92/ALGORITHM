cnt = 2
num = 5

def prime(num):
    while num % 2:
        for i in range(3, num, 2):
            if num % i == 0:
                return False
        return True

while cnt != 10001:
    if prime(num):
        cnt += 1
    num += 1

print(num-1)