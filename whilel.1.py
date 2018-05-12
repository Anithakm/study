'''Calculate the sum of digits of a number given by user. E.g.-
INUPT : 123        OUPUT : 6
INUPT : 12345        OUPUT : 15'''

num=int(input("enter the no\n"))
sumn=0
#number%10 will give last digit of number
#number = number/10 will give new number without that digit
#we will stop when number will be smaller than 10
while True:
    r=num%10
    num=num/10
    sumn=sumn+r
    if num<10:
        sumn=sumn+num
        break
print(sumn)
