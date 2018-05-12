#Find largest and smallest elements of a list.
a=[777,34,333,234]
i=0

largest=a[0]
while i<len(a):
    if a[i]>largest:
        largest=a[i]
    i=i+1
print(largest) 
j=0

smallest=a[0]
while j<len(a):
    if a[j]<smallest:
        smallest=a[j]
    j=j+1
print(smallest) 
