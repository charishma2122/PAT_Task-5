# Define the number of levels in the pyramid
py_max = 20  # Assigning the highest value to variable to iterate the pyramid
# Outer loop to iterate through each level
for i in range(1, py_max + 1):
    # Print leading spaces to center-align the numbers
    for j in range(py_max - i):
        print("  ", end=" ")
    # display numbers in ascending order up to the current level
    for j in range(1, i + 1):
        print(j, end=" ")
    # display numbers in descending order from (i-1) down to 1
    for j in range(i - 1, 0, -1):
        print(j, end=" ")
    # Move to the next line for the next level
    print()