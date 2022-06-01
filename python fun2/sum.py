def sum(*a):
    total =0
    for x in a:
        total = total+x
    
    print("sum", total)

sum(10)
sum(10,20)
sum(10,20,30)