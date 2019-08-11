# codewars - Regex validate PIN code

def validate_pin(pin):
    for i in range(len(pin)):
        testi = str(pin)[i]
        try:
            int(testi)
        except:
            return False
    if len(pin) == 4 or len(pin) == 6:
        return True
    else:
        return False

print(validate_pin("2343\n"))


def validate_pin(pin):
    return len(pin) in (4, 6) and pin.isdigit()

import re
def validate_pin(pin):
    return bool(re.match(r'^(\d{4}|\d{6})$',pin))