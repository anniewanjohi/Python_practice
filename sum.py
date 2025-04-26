def sum_of_digits(n):
   s=0
   while n>0:
    d=n%10
    s=s+d
    n=n//10
   return s
n=int(input("Enter a number:"))
result=sum_of_digits(n)
print ("Sum of digits",result)
