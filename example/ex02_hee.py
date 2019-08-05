def calc(equation):
   li = equation.split('+')
   sum_li = []
   if li[0] == '':
       li.remove('')
   elif int(li[0]) < 0:
       sum_li.append(int(li[0]))
   sub_li = []
   sub_li_2 = []
   for i in li[1:]:
       if i.isdigit():
           sum_li.append(int(i))
       else:
           sub_li = i.split('-')
           for idx, s in enumerate(sub_li):
               if idx % 2 == 1:
                   sub_li_2.append(int(s))
               else:
                   sum_li.append(int(s))
   return (sum(sum_li) - sum(sub_li_2))

print(calc('1+1'))
print(calc('1-1'))
print(calc('123+2-124'))
print(calc('-12+12-7979+9191'))
print(calc('+1-1+1-1+1-1+1-1+1-1+1-1+1-1+1-1+1-1+1-1+1-1+1-1+1-1+1-1+1-1+1-1'))
