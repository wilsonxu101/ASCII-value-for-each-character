# Get string from othe user
user_string = input("Enter a string to get the ASCII values: ")
str_length = len(user_string)

# Print string's ASCII values
for i in range(str_length):  # i by convention is short for "index"
    c = user_string[i]       # c by convention is short for "character"
    ascii_value = ord(c)     # get the ordinal value
    print("character '" + c + "' has the ASCII value", ascii_value)

# Print string's ASCII values in reverse
print("Starting from the end...")
# starting index -1, going to the last index, incrementing by -1 each time.
for i in range(-1, -(str_length+1), -1):
    c = user_string[i]
    ascii_value = ord(c)
    print("character '" + c + "' has the ASCII value", ascii_value)
