f=open('loc.jpeg','rb')
bytes = f.read()


f = open('newloc.jpeg', 'wb')
f.write(bytes)
f.close()