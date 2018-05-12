#A company decided to give bonus of 5% to employee if his/her year of service is more than 5 years.
#Ask user for their salary and year of service and print the net bonus amount.
print("enter salary")
salary=int(input())
print("enter years")
years=int(input())

if(years>5):
    print("net bonus is",(.05*salary))
else:
    print("no bonus")
