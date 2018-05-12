'''Make a list by taking 10 input from user. Now delete all repeated elements of the list.
E.g.-
INPUT : [1,2,3,2,1,3,12,12,32]
OUTPUT : [1,2,3,12,32]'''
a=[1,2,2,3,4,5,5,6]
i=0
print(a)
while i<len(a):
    j=i+1
    while j<len(a):
        if a[i]==a[j]:
            del(a[j])
        j=j+1
    i=i+1
print("the new list is",a)
