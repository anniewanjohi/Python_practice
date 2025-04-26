#computing the factorial of a number using for loop
num =int(input("Enter an integer number:"))
fact=1
for i in range(1,num+1):
    fact=fact*i
print("The factorial of",num,"is",fact)
