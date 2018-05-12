#Take 3 inputs from user and check :all are equal ,any of two are equal
#( use and or )
print("enter a")
a=input()
print("enter b")
b=input()
print("enter c")
c=input()

all=a==b and b==c and c==a
print("all are equal",all)

any=a==b or b==c or c==a
print("any of two are equal",any)
