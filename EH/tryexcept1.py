a = int(input("Enter First Number:"))
b = int(input("Enter Second Number:"))
try:
    print(a/b)
except ZeroDivisionError as err:
    print(err)
