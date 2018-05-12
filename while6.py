'''Write a program to find greatest common divisor (GCD)
or highest common factor (HCF) of given two numbers.'''
x=int(input("enter the first no\n"))
y=int(input("enter the second no\n"))
#x,y=10,20 means x=10 y=20
while y!=0:
    x,y=y,x%y
print(x)
