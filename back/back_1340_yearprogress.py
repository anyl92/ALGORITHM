import sys
sys.stdin = open('1340.txt', 'r')

inp_list = (input().replace(', ', ' ').replace(':', ' ')).split()
print(inp_list)

month_list = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']

year = int(inp_list[2])
month = month_list.index(inp_list[0])
day = int(inp_list[1])
hour = int(inp_list[3])
minute = int(inp_list[4])

year_type = 0  # 0 기본 1 윤년
if (year % 400 == 0) or (year % 4 == 0 and year % 100 != 0):
    year_type = 1
print(year_type)

if year_type:  # 윤년이면
    all_day = 366 * 24 * 3600
else:
    all_day = 365 * 24 * 3600
print(all_day)

month_dp = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
month_dp = [x*24*60 for x in month_dp]
for y in range(1, len(month_dp)):
    month_dp[y] = month_dp[y] + month_dp[y-1]
print(month_dp)
cur_day = minute + (hour*60) + (day*24*60) + (month_dp[month])
print(cur_day)

print(cur_day / all_day * 100)
