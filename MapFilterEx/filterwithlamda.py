prices = [599,99,499,1999,4999,5999,799]


def check(price):
    return price<1000

print(list(filter(check, prices)))

