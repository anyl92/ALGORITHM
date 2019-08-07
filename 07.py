# codewars - Who likes it?

def likes(names):
    repeat = 'like this'
    str_name = ' '.join(names)

    if not names:
        return f'no one like this'

    elif ' ' not in str_name:
        name = names.pop(0)
        return f'{name} like this'

    elif str_name.count(' ') == 1:
        return f'{names[0]} and {names[1]} {repeat}'

    elif str_name.count(' ') == 2:
        return f'{names[0]}, {names[1]} and {names[2]} {repeat}'

    else:
        pop1 = names.pop(0)
        pop2 = names.pop(0)
        return f'{pop1}, {pop2} and {len(names)} others {repeat}'

    Test.assert_equals(likes(names[:]),sol(names),"It should work for random inputs too")

print(likes([]))  #'no one likes this'
print(likes(['Peter']))  #'Peter likes this'
print(likes(['Jacob', 'Alex']))  # 'Jacob and Alex like this'
print(likes(['Max', 'John', 'Mark']))  # 'Max, John and Mark like this'
likes(['Alex', 'Jacob', 'Mark', 'Max'])  # 'Alex, Jacob and 2 others like this'