#Take input of age of 3 people by user and determine
#oldest and youngest among them.
print("enter age of a")
a=int(input())
print("enter age of b")
b=int(input())
print("enter age of c")
c=int(input())
if(a>b and a>c):
    print("oldest is",a) 
elif(b>a and b>c):
    print("oldest is",b)
elif(c>a and c>b):
    print("oldest is",c)
else:
    print("all are equal")
    
