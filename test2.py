decimal_number = 3  # Example decimal number

binary_number = bin(decimal_number)[2:].zfill(5)  # Convert to binary and pad with leading zeros
print(binary_number)