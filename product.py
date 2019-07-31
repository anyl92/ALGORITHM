A = input()
B = input()

one_line = int(A) * int(B[2])
two_line = int(A) * int(B[1]) * 10
three_line = int(A) * int(B[0]) * 100

print(int(A) * int(B[2]))
print(int(A) * int(B[1]))
print(int(A) * int(B[0]))
result = one_line + two_line + three_line
print(result)
