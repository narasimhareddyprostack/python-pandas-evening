a = int(input("Enter First Number:"))  
b = int(input("Enter Second Number:"))
c = int(input("Enter Third Number:"))
if a>b and a>c:
    print("Max Number:",a)
elif b>a and b>c:
    print("Max Number:",b)
else:
    print("Max Number",c)