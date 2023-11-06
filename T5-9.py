string= input("Enter string: ") # Taking input from user
char=0 # initializing the characters to 0
word=1 # initializing the words to 1
for i in string: # The for loop is used to traverse through the characters in the  givenstring
      char=char+1 # Incrementing the character based on the length
      if(i==' '): #Checking if the given string has any space
            word=word+1 #If we found space incremeting the word sount
print("Number of words in the string:",word)
print("Number of characters in the string:",char )