def longest_common_substring(str1, str2):
    m = len(str1)
    n = len(str2)
    # Create a table to store the length of the common substring
    dp = [[0] * (n + 1) for _ in range(m + 1)]
    # Variables to keep track of the length of the longest common substring and its ending position
    max_length = 0
    end_position = 0

    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if str1[i - 1] == str2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
                if dp[i][j] > max_length:
                    max_length = dp[i][j]
                    end_position = i
            else:
                dp[i][j] = 0

    # Extract the longest common substring
    longest_substring = str1[end_position - max_length:end_position]

    return longest_substring

# Example usage:
str1 =  input("Enter string : ") #"abcdefg"
str2 =  input("Enter string : ") # "acdef"
result = longest_common_substring(str1, str2)
print("Longest Common Substring:", result)
