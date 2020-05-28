a = 1
answer = 0
for _ in range(1000):
  a *= 2

while a > 0:
  answer += (a % 10)
  a //= 10

print(answer)