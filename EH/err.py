try:
    f = open('harish.txt','r')
    data= f.read()
    print(data)
except:
    f = open('default.txt','r')
    data = f.read()
    print(data)