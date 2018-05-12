'''Take 10 integer inputs from user and store
them in a list and print them on screen'''
i=10
a=[]
while i>=0:
    num=int(input("enter number: "))
    a.append(num)
    i=i-1
print(a)
