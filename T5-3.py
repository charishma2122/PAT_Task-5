def remove_vowels(input_string): # Function assignemnt with the input to be passed
    vowels = "aeiou" # we defined the vowels
    result = "" # initialised the empty output
    for char in input_string: # checking the each letter  in the sentence
        if char not in vowels: # if the letter is not vowel
            result += char # add that letter to  result variable
    return result # after iterating the entire string, final string will be stored
# Example usage:
input_string = input("Enter string : ")#"Guvi Geeks Network Private Limited" # Input string assigned to a variable
input_string = input_string.lower()
result = remove_vowels(input_string) #  calling the function and assigning the input string to function
print("'After removing the vowels in the given string' :",result)  # Final output to display after removing the vowels in the given string