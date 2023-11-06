# my_string = "Python-Interpreter"
my_string= input("Enter string : ") # Taking input from the user and assiging to a variable
my_string = my_string.lower() # converting given string to lower cases
max_string = {} # An empty dictionary is created
for i in my_string: #  The letters in the string are iterated over
   if i in max_string: #
      max_string[i] += 1 # and if it has been matched to a character, it is incremented
   else:
      max_string[i] = 1 # Else, it is assigned to 1.
my_result = max(max_string, key = max_string.get) # The maximum of the values in the dictionary is determined.
print ("The maximum of all characters is : ",my_result)