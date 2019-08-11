import math


def bisection(n, minimum=0, maximum=1):
    while not math.isclose(minimum, maximum):
        if minimum ** 2 == n:
            return minmum
        elif maximum ** 2 == n:
            return maximum
        elif minimum ** 2 < n < maximum ** 2:
            guess = (minimum + maximum) / 2
            if n > guess ** 2:
                minimum = guess
            else:
                maximum = guess
        else:
            minimum, maximum = maximum, maximum + 1
    return minimum

# print(bisection(3))


def bis(n, minimum=0, maximum=1):
    if minimum ** 2 == n:
        return minmum
    elif maximum ** 2 == n:
        return maximum
    elif math.isclose(minimum, maximum):
        return minimum

    if minimum ** 2 < n < maximum ** 2:
        guess = (minimum + maximum) / 2
        if n < guess ** 2:
            return bis(n, minimum, guess)
        else:
            return bis(n, guess, maximum)
    else:
        minimum, maximum = maximum, maximum + 1
        return bis(n, minimum, maximum)

print(bis(34), 34 ** (1/2))
