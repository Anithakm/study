'''Take 10 integer inputs from user and store them in a
list. Now, copy all the elements in
another list but in reverse order.'''
i=5
a=[]
while i>0:
    num=int(input("enter no:"))
    a.append(num)
    i=i-1
a.reverse()
print(a)
