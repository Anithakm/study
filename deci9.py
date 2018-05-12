'''Modify the above question to allow student to
sit if he/she has medical cause.
Ask user if he/she has medical cause or not ( 'Y' or 'N' ) and
print accordingly.'''
print("no of class held")
noh=int(input())
print("enter no of class attend")
noa=int(input())
atten=(noa/float(noh))*100

medical_cause=input("is she medical cause?Y or N : ")

if(medical_cause=='Y'):
    print("you are allowed")
else:
    if(atten>=75):
        print("allowed")
    else:
        print("not allowed")
        
