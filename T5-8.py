string1 = input("Enter string1: ") #"listen"
string2 = input("Enter string2: ") #"silent"
string1=list(string1) # creating a list for string1
string1.sort() # sort method sorts the list  to ascending order
string2 = list(string2) #creating a list for string2
string2.sort()
if string1 == string2: # checking the given strings is equal
   print ("Given Strings are Anagram") # if that are equal, the output was anagram
else:
   print ("Given String are not anagrams") #if the two strings are not equal, the output was not a anagram