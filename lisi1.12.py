'''Ask user to give integer inputs to make a list.
Store only even values given and print the list.'''
a=[]

print("enter the no 1")
num1=int(input())
print("enter the no 2")
num2=int(input())
print("enter the no 3")
num3=int(input())

if num1%2 == 0:
    a.append(num1)
if num2%2 == 0:
    a.append(num2)
if num3%2 == 0:
    a.append(num3)
print(a)
