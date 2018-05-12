'''write a program to print sum, average of all numbers,
smallest and largest element of a list.'''
a=[1,2,3,4,5]
sum=0
i=0
avg=0
print(a)
while i<len(a):
    sum=sum+a[i]
    avg=sum/a[i]
    i=i+1
print("sum of elements of the list is:",sum)
print("average of the list is",avg)

i=0
largest=a[0]
while i<len(a):
    if a[i]>largest:
        largest=a[i]
    i=i+1
print("largest element is ",largest)

j=0
smallest=a[0]
while j<len(a):
    if a[j]<smallest:
        smallest=a[j]
    j=j+1
print("smallest element is",smallest) 
