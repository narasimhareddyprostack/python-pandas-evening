l1 = [4,7,8,6,14,27,37]
def is_Even(x):
    if x % 2 ==0:
        return True
    else:
        return False
l2 = list(filter(is_Even, l1))
print(l1)
print(l2)