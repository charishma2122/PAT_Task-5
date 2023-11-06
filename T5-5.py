
def palindrome_check(my_string):  # Function assignemnt with the input to be passed  # checking the each character in the input string
   if (my_string == my_string[::-1]):  # checking if my_string is equal to when we reverese the string
      print("The string is a palindrome")  # If both are matched it is a palindrome
   else:
      print("The string isn't a palindrome")  # else not a palindrome
my_string=input("Enter string to check if it palidrome: ") # Taking input from the user and assiging to a variable
my_string = my_string.lower() # converting a given i/p string to lower cases  to avoid the case sensitives
result = palindrome_check(my_string)







