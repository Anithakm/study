'''A 4 digit number is entered through keyboard.
Write a program to print a new number with digits
reversed as of orignal one. E.g.-
INPUT : 1234        OUTPUT : 4321
INPUT : 5982        OUTPUT : 2895'''

number=int(input("enter the 4digit number: \n"))

#seperating digits of the number
#1234/1000 = 1
#1234%1000 = 234

first_number = number/1000
rem = number%1000

#234/100 = 2
#234%100 = 34
second_number = rem/100
rem = rem%100

#34/10 = 3
#34%10 = 4
third_number = rem/10
fourth_number = rem%10

#creating new number with digits reversed
#1234 = (1*1000)+(2*100)+(3*10)+4 i.e., 1000+200+30+4
new_number = (fourth_number*1000)+(third_number*100)+(second_number*10)+(first_number)
print(new_number)
