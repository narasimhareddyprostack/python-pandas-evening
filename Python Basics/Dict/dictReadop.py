emp =  {'id':101,'name':"Rahul",'sal':45000, 'loc':'wayanad'}
print(emp)

#print keys
for x in emp:
    print(x)
print("*****************")
#print values
for x in emp:
    print(emp[x])
print("*****************")

for x in emp:
    print(x,":",emp[x])