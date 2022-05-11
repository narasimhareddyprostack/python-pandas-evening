s = {10,"Rahul",10}
'''
for x in s:
    print(x)
    
#print(s)
'''
# TypeError: 'set' object is not subscriptable
i = 0
while i<=len(s)-1:
    print(s[i])
    i = i+1