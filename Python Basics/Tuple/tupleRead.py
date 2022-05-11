l  = []  # Mutable object
t  = ()  # read only version of list/Immutable Obj

l.append(10)
t.append(10)   # AttributeError
