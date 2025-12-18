def add(a,b):
    return a+b
def subtract(a,b):
    return a-b
print("Enter 1 or 2")
choice=int(input("Enter Choice"))
a=float(input("Enter 1st number"))
b=float(input("Enter 2nd number"))
if choice==1:
    print(add(a,b))
else:
    print(subtract(a,b))
