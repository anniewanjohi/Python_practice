def reverse_sring(string):
#initializing an empty string
    reversed_string=""
      #looping through the string from the last char to the first
    for i in range(len(string)-1,-1,-1):
      reversed_string+= string[i]
    return reversed_string
user_input=input("Enter  a string:")
new_string=reverse_sring(user_input)
print("Reversed string:",new_string)
