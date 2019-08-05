#codewars - Vasya - Clerk

def tickets(people):
    vasya_have = 0
    money_25 = money_50 = money_100 = 0
    for i in people:
        if i == 25:
            money_25 += 1
        elif i == 50:
            money_50 += 1
            money_25 -= 1
        elif i == 100:
            if money_50 < 1 and money_25 > 1:
                money_25 -= 2
            money_100 += 1
            money_25 -= 1
            money_50 -= 1                    
    if money_25 < 0 or money_50 < 0:    
        return 'NO'
    else:
        return 'YES'

# def tickets(people):
#     have = 0
#     for i in people:
#         have += i
#         if i > 25:
#             change = i-25
#             print(change)
#             if change > have:
#                 return "NO"
#             else:
#                 have -= change
#     return "YES"

print(tickets([25, 25, 50]))
print(tickets([25, 100]))
print(tickets([25, 25, 50, 50, 100]))