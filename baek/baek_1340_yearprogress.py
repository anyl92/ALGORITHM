import sys
sys.stdin = open('1340.txt', 'r')

inp_list = (input().replace(', ', ' ').replace(':', ' ')).split()

month_list = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
month = month_list.index(inp_list[0]) + 1

month_dp = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
month_dp = [x*24*60 for x in month_dp]
for y in range(2, len(month_dp)):
    month_dp[y] = month_dp[y] + month_dp[y-1]

year = int(inp_list[2])
day = int(inp_list[1]) - 1
hour = int(inp_list[3])
minute = int(inp_list[4])

year_type = 0  # 0 기본 1 윤년
if (year % 400 == 0) or (year % 4 == 0 and year % 100 != 0):
    year_type = 1

if year_type:
    all_minute = 366 * 24 * 60
else:
    all_minute = 365 * 24 * 60

cur_minute = minute + (hour*60) + (day*24*60) + (month_dp[month-1])
if year_type and month > 2:
    cur_minute += 1440

print(cur_minute / all_minute * 100)
