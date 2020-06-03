a = 2 ** 1000
answer = 0

while a > 0:
  answer += (a % 10)
  a //= 10

print(answer)