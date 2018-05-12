#Write a program to find the sum of all elements of a list.
a=[1,2,3,4,5]
sum=0
i=0
print(a)
while i<len(a):
    sum=sum+a[i]
    i=i+1
print("sum of elements of the list is:",sum)
