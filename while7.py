'''Take integer inputs from user
until he/she presses q ( Ask to press q to quit after every integer input )
. Print average and product of all numbers.'''

count =0
total=0
ask=input ("Do you want to enter a number? (Y/N)")
while ask=="Y":
    numbers=float(input("Enter number"))
    count= count+1
    total=total+numbers
    con_ask=input ("Do you want to continue entering a number? (Y/N)")
    if con_ask=="Y":
        numbers=float(input("Enter number"))
        count=count+1
        total=total+numbers
    elif con_ask=="N":
print("The average of", count, "numbers is", total/count)
