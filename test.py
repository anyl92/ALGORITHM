# def step_down(dist, step):
#     down = []
#     cnt = dist[0]
#
#     while dist:
#         while dist and dist[0] == cnt and len(down) < 3:
#             down.append(step + 1)
#             dist.pop(0)
#
#         for k in range(len(down)):
#             down[k] -= 1
#
#             if down[k] <= 0 and dist and dist[0] < cnt:
#                 down[k] = step
#                 dist.pop(0)
#
#         for i in down:
#             if i == 0:
#                 down.pop(i)
#
#         cnt += 1
#     print(cnt + max(down))
#     return cnt + max(down)

# dist = [3, 6, 7, 8]
# dist = [2, 2, 2, 3]
# dist = [2, 4, 6, 7]

# dist = [4, 7]
# dist = [3, 3, 6, 7, 8]

# dist = [6, 3]
# dist = [4, 5, 4, 12, 7]

# step_down([6, 3], 7)

a = []
print(a[0])