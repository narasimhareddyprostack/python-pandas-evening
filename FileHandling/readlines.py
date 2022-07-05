f = open("one.txt",'r')
data = f.readlines()
print(type(data))
for x in data:
    print(x)

#print(data)

f.close()