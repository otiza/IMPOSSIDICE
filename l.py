# Hexadecimal values as strings
hex_start = "0x3ffffde7210bd00e5"
hex_end = "0x3ffffffffffffffff"

# Convert hexadecimal strings to integers
start = int(hex_start, 16)
end = int(hex_end, 16)

# Calculate the number of integers in the range (inclusive)
count = (end - start) + 1

# Print the result
print(f"Number of integers between {hex_start} and {hex_end}: {count}")