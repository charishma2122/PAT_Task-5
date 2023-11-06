# Part a we will assign a string to variable and check how many total vowels were present in the string
vowels = ['a', 'e', 'i', 'o', 'u'] # Vowels can be capital or small letters
string = ("Guvi Geeks Network Private Limited") # assign the string to a variable
print(string)
string = string.lower() # we converted all letter to lower case letters. we can convert upper cases by using upper function
print("Converted the string to lower cases",string)
count = 0 # initializing the counter
for letter in string: # checking the each letter  in the sentence
    if letter in vowels: # if the letter in vowel is matched, then we will increase the counter from 0 to max
        count += 1 # This loop will iterate untill each letter is completed in the assigned string
print("Total vowels count",count) # final output will be displayed i.e, how many vowels present in the given string
print("count of a vowel: ",string.count('a'))  #This will count letter a in the asssigned string
print("count of e vowel: ",string.count('e')) #This will count letter e in the asssigned string
print("count of i vowel: ",string.count('i')) #This will count letter i in the asssigned string
print("count of o vowel: ",string.count('o')) #This will count letter o in the asssigned string
print("count of u vowel: ",string.count('u')) #This will count letter u in the asssigned string
