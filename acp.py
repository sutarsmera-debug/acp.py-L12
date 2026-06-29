def decimal_to_binary(n):
    if n ==0:
        return "0"
    
    binary_str = ""
    while n > 0:
        remainder = n % 2
        binary_str = str(remainder) + binary_str
        n = n // 2  
    return binary_str

# test the program
decimal_number = 13
result = decimal_to_binary(decimal_number)
print(f"The binary of {decimal_number} is {result}")
# output: The binary of 13 is 1101  