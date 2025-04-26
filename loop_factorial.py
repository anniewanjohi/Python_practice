#computing the factorial of a number using for loop
num =int(input("Enter an integer number:"))
#intializing the variable fact to 1
fact=1
#range -creates a sequence from 1 upto the number
for i in range(1,num+1):
    fact=fact*i
print("The factorial of",num,"is",fact)
