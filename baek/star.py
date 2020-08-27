import sys
sys.stdin = open('star.txt', 'r')

# # 2438
# N = int(input())
# for i in range(1, N+1):
#     print('*' * i)

# # 2439
# N = int(input())
# for i in range(1, N):
#     print(' ' * (N-i) + '*' * i)
# print('*' * N)

# # 2440
# N = int(input())
# for i in range(N):
#     print((N-i) * '*')

# # 2441
# N = int(input())
# for i in range(N):
#     print(' ' * i + '*' * (N-i))

# # 2442
# N = int(input())
# for i in range(1, N+1):
#     print((N-i)*' ' + (2*i-1)*'*')

# # 2443
# N = int(input())
# for i in range(N, 0, -1):
#     print((N-i)*' ' + (2*i-1)*'*')

# # 2444
# N = int(input())
# for i in range(1, N):
#     print((N-i)*' ' + (2*i-1)*'*')
# for i in range(N, 0, -1):
#     print((N-i)*' ' + (2*i-1)*'*')

# # 2445
# N = int(input())
# for i in range(1, N):
#     print(i*'*' + ((N-i)*2)*' ' + i*'*')
# print((N*2)*'*')
# for i in range(N-1, 0, -1):
#     print(i*'*' + ((N-i)*2)*' ' + i*'*')

# # 2446
# N = int(input())
# for i in range(N):
#     print(i*' ' + (2*(N-i)-1)*'*')
# for i in range(2, N+1):
#     print((N-i)*' ' + (2*(i)-1)*'*')

# 2447
N = int(input())
