def unique_chars (input_string): #Function assignemnt with the input to be passed
    count_uni_chars = "" # Count of unique characters
    final_unique_chars = "" # initializing and variable to pass the final  unique characters into it
    for i in input_string: # checking the each character in the input string
        if i not in final_unique_chars: # checkinh here i values is not repetative in the final_unique_ characters
            count_uni_chars += i # if it unique it will increment the count of unique characters
            final_unique_chars += i # if characteris  unique it will increment the final_unique_characters
    print("count of unique charaters",len(count_uni_chars))
    print(" 'Final unique charaters:' ",final_unique_chars)
input_string = input("Enter string : ") # Input string assigned to a variable
input_string = input_string.lower()
result = unique_chars(input_string) #  calling the function and assigning the string to function