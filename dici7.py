#Write a program to print absolute vlaue of a number entered by user. E.g.-
#INPUT: 1        OUTPUT: 1
#INPUT: -1        OUTPUT: 1
print("Enter a number")
number = int(input())
if number<0:
  print(number*-1)
else:
  print(number)
	
