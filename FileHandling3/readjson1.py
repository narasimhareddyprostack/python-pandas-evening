import json

f = open('data.json','r')
data=json.load(f)
print(data)
print(f.closed)   #false
f.close()
print(f.closed)   #true