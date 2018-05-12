'''Write a program to find prime factor of a number.
If a factor of a number is prime number then it is its prime factor.'''
num=int(input("enter the no: "))
i=2
while i<=num:
    j=2
    count=0
    while j<=i:
        if i%j==0:
            count=count+1
        j=j+1
    #if count>1 then it is not prime
    # if prime and factor(num%i==0) then it is prime factor
    if count<=1 and num%i==0:
        print(i)
    i=i+1
        
