import datetime
def convert_to_binary_floating_point(number, num_bits=14):
    # Step 1: Determine the sign bit
    sign_bit = '0' if number >= 0 else '1'
    number = abs(number)

    # Step 2: Convert the integer part and fractional part to binary
    integer_part = bin(int(number))[2:]
    fractional_part = ''
    fractional_value = number - int(number)

    while len(fractional_part) < 8:  # Limit the mantissa to 8 bits
        fractional_value *= 2
        bit = '1' if fractional_value >= 1.0 else '0'
        fractional_part += bit
        if fractional_value >= 1.0:
            fractional_value -= 1.0

    # Trim trailing zeros from the fractional part
    fractional_part = fractional_part.rstrip('0')

    # Step 3: Adjust the binary point
    binary_value = integer_part + '.' + fractional_part

    # Step 4: Adjust the exponent
    exponent = len(integer_part) - 1  # Adjust for the implicit leading '1'

    # Step 5: Combine the sign bit, exponent, and mantissa
    mantissa = fractional_part[:8]  # Limit the mantissa to 8 bits

    # Ensure the mantissa is of the desired length
    mantissa = mantissa.ljust(8, '0')

    # Format the final binary representation
    binary_representation = f"{sign_bit}_{exponent:05b}_{mantissa}"

    return binary_representation


# Ask the user to input a decimal number
decimal_number = float(input("Enter a decimal number: "))

# Get the current date and time
current_datetime = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')

# Convert the decimal number to a 14-bit binary floating-point representation
binary_representation = convert_to_binary_floating_point(decimal_number)

# Display the result with date and time
print(f"{decimal_number} in 14-bit binary floating-point: {binary_representation} (as of {current_datetime})")
