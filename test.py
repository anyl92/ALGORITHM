basket = {
    'apple': 4, 'orange': 3, 'computer': 28,
    'tv': 2, 'banana': 5, 'tomato': 9
    }
fruits = ['apple', 'orange', 'banana', 'pear', 'tomato']

total_fruits = 0
total_nofruits = 0
for i, j in basket.items():
    if i in fruits:
        total_fruits += j
    elif i not in fruits:
        total_nofruits += j
print(f'과일은 {total_fruits}개, 아닌 것은 {total_nofruits}개입니다.')
