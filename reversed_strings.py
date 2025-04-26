string=input("Enter a string:")
#initializing an empty string
reversed_string=""
#looping through the string from the last char to the first
for i in range(len(string)-1,-1,-1):
    reversed_string+=string[i]
print("Reversed string:",reversed_string)