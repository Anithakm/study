#Write a program to find the product of all elements of a list.
a=[1,2,3,7]
pro=1
i=0
print(a)
while i<len(a):
    pro=pro*a[i]
    i=i+1
print("product of the list is:",pro)
