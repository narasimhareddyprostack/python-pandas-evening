def evennum(n):
    return n%2 ==0

obj = filter(lambda n:n%2 ==0, range(0,10))
result = list(obj)
print(result)

#print(list(filter(evennum,range(0,10))))