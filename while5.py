'''Factorial of any number n is represented by n! and is equal to 1*2*3*....*(n-1)*n. E.g.-
4! = 1*2*3*4 = 24
3! = 3*2*1 = 6
2! = 2*1 = 2
Also,
1! = 1
0! = 0
Write a program to calculate factorial of a number.'''

no=int(input("enter the no\n"))
fac=1
if(no==0):
    print(1)
else:
    while no>=1:
        fac=fac*no
        no=no-1
    print(fac)
    
    
