'''Write a program to print a number given by user but digits reversed. E.g.-
INPUT : 123        OUTPUT : 321
INPUT : 12345        OUTPUT : 54321'''
n=int(input("Enter number: "))
rev=0
while(n>0):
    dig=n%10
    rev=rev*10+dig
    n=n//10
print("Reverse of the number:",rev)
