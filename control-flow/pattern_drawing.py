# Prompt the user to enter the size of the pattern
pattern_size = int(input("Enter the size of the pattern: "))

# Draw the Pattern
row = 0
while row < pattern_size:
    col = 0
    while col < pattern_size:
        print("*", end="")
        col += 1
    print()  # Move to the next row
    row += 1
