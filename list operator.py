#list operation
subjects=['physics','chemistry','maths','biology']
print(subjects)
print("index of first  in the list is",subjects[0])
print("index of 2nd  in the list is",subjects[1])
print("index of 3rd  in the list is",subjects[2])
print("index of 4th  in the list is",subjects[3])
print(subjects[0:1])
print(subjects[1:3])


#other example of list
lst1 = ['computersc', 'IT', 'CSE',34]
lst2 = [1993, 2016]
lst3 = [2, 4, 6, "g", "k", "s"]

print(lst1)
print("lst1[0]", lst1[0])
print("lst3[2:4]", lst3[2:4])
   
#update the list

lst1[1]="robotics"
print("updated value of 2nd index is",lst1[1])

print(lst1)

#delete the elements from the list
del lst1[2]
print(lst1)
