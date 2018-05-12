'''Write all Armstrong numbers between 100 to 500.'''
#lower_Range = int(input("Enter lower range : "))  
#upper_Range = int(input("Enter upper range : "))  
  
for n in range(100,500):  
   sum = 0  
   temp = n  
   while temp > 0:  
       digit = temp % 10  
       sum = sum + digit ** 3  
       temp = temp // 10  
  
   if n == sum:  
       print(n)   
