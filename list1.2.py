'''Take 10 integer inputs from user
and store them in a list. Again ask user to give a number.
Now, tell user whether that number is present in list or not.
( Iterate over list using while loop ).'''
i=10
a=[]
while i>0:
    num=int(input("enter no:"))
    a.append(num)
    i=i-1
print(a)
n=int(input("enter no: "))

'''i=9
count=0
while i>=0:
    if n==a[i]:
     print("yes")
     count=count+1
    i=i-1
if count==0:
    print("no")

if n in a:
    print("yes")
else:
    print("no")'''
if n in a:
    print("yes")
else:
    print("no")
