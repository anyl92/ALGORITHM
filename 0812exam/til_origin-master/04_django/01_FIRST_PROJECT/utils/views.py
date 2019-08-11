from django.shortcuts import render, HttpResponse
import random


def cube(request, num):
    # 기본 자료형은 return 안됨!
    r = num ** 3
    context = {'result': r}
    return render(request, 'cube.html', context)


def check_int(request, num):
    is_even = num % 2 == 0
    return render(request, 'check_int.html', {
        'is_even': is_even,
        'num': num,
    })


def pick_lotto(request):
    lucky_numbers = random.sample(range(1, 46), 6)

    return render(request, 'pick_lotto.html', {
        'lucky_numbers': lucky_numbers,
    })