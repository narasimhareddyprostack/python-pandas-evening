def f1():
    a=10
    global b
    b=20
    print(a+b)
f1()
def f2():
    a=10
    print(a+b)
f2()