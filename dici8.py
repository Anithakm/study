'''A student will not be allowed to sit in exam if his/her attendence
is less than 75%.
Take following input from user
Number of classes held
Number of classes attended.
And print
percentage of class attended
Is student is allowed to sit in exam or not.
'''
print("enter no of classes held")
class_held=int(input())

print("enter no of classes attended")
class_attend=int(input())

attend=(class_attend/float(class_held))*100
print("class attended is",attend)

if(attend>75):
    print("student allowed in exam")
else:
    print("student not allowed in exam")
