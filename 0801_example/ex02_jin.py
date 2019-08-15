def calc(equation):
#     a = ''.join(equation)
#     return a
   equation = list(equation)
   num_list = []
   num_sum = []
   math_list = []
   num='1234567890'
   pos=0
   if equation[0] == '-':
       pos += 1
   for i in equation:
       if i in num:
           num_list += i
           num_list = ''.join(num_list)
       else:
           math_list += i
           num_sum.append(num_list)
           num_list = []
   else:
       num_sum.append(num_list)
   def summmmmmmmm(num_sum, math_list, pos):
       result = 0
       if pos == 1:
           result = result-int(num_sum[1])
           for i in range(1,len(math_list)):
               j = i + 1
               if math_list[i]== '+':
                   result = result + int(num_sum[j])
               else:
                   result = result - int(num_sum[j])
       else:
           result = result+int(num_sum[0])
           for i in range(len(math_list)):
               j = i + 1
               if math_list[i]== '+':
                   result = result + int(num_sum[j])
               else:
                   result = result - int(num_sum[j])
       return result
   result = summmmmmmmm(num_sum, math_list, pos)
   return result