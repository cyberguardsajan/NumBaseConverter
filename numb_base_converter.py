    print("""
    
  _   _                 ____                  ____                          _            
 | \ | |_   _ _ __ ___ | __ )  __ _ ___  ___ / ___|___  _ ____   _____ _ __| |_ ___ _ __ 
 |  \| | | | | '_ ` _ \|  _ \ / _` / __|/ _ \ |   / _ \| '_ \ \ / / _ \ '__| __/ _ \ '__|
 | |\  | |_| | | | | | | |_) | (_| \__ \  __/ |__| (_) | | | \ V /  __/ |  | ||  __/ |   
 |_| \_|\__,_|_| |_| |_|____/ \__,_|___/\___|\____\___/|_| |_|\_/ \___|_|   \__\___|_|   
                                                                                         
""")

    print("Choose the type of input number:")
    print("1. Decimal")
    print("2. Binary")
    print("3. Octal")
    print("4. Hexadecimal")
    choice = int(input("Enter your choice (1-4): "))

    if choice == 1:
        num = int(input("Enter a decimal number: "))
        print(f"Binary: {bin(num)[2:]}")
        print(f"Octal: {oct(num)[2:]}")
        print(f"Hexadecimal: {hex(num)[2:].upper()}")

    elif choice == 2:
        num = input("Enter a binary number: ")
        decimal_num = int(num, 2)
        print(f"Decimal: {decimal_num}")
        print(f"Octal: {oct(decimal_num)[2:]}")
        print(f"Hexadecimal: {hex(decimal_num)[2:].upper()}")

    elif choice == 3:
        num = input("Enter an octal number: ")
        decimal_num = int(num, 8)
        print(f"Decimal: {decimal_num}")
        print(f"Binary: {bin(decimal_num)[2:]}")
        print(f"Hexadecimal: {hex(decimal_num)[2:].upper()}")

    elif choice == 4:
        num = input("Enter a hexadecimal number: ")
        decimal_num = int(num, 16)
        print(f"Decimal: {decimal_num}")
        print(f"Binary: {bin(decimal_num)[2:]}")
        print(f"Octal: {oct(decimal_num)[2:]}")

    else:
        print("Invalid choice. Please select a valid option.")
