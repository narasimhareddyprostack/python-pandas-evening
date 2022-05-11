def verify(func):
    def inner(name):
        if name=="Modi":
            print(name,":India Prime Minister")
        else:
            func(name)
    return inner

def employee(name):
    print("Hi",name, ",GM")

verifyEmployee = verify(employee)

employee("Modi")  #decorator wont be executed
employee("Rahul") #decorator wont be executed

verifyEmployee("Modi") #decorator will be executed
verifyEmployee("Rahul")#decorator will be executed
