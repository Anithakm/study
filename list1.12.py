'''Take a list of 10 elements. Split it into
middle and store the elements in two dfferent lists.'''
a = [58,24,13,15,63,9,8,81,1,78]
b = len(a)/2
print(a[:int(b)])
print(a[int(b):])
