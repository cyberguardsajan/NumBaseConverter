
# NumBaseConverter - Documentation

This documentation is intended to outline the important and complex aspects of the `NumBaseConverter` program for future reference for myself.

## Overview

The `NumBaseConverter` program performs numerical base conversions between decimal, binary, octal, and hexadecimal formats. 
It provides an interactive interface allowing users to input a number and receive its representation in the other three bases.

## Code Explanation

### User Choice

The program prompts the user to select the base of the number they wish to convert. The available choices are:

```python
print("Choose the type of input number:")
print("1. Decimal")
print("2. Binary")
print("3. Octal")
print("4. Hexadecimal")
choice = int(input("Enter your choice (1-4): "))
```

### Conversion Logic

Based on the user's choice, the program handles the conversion as follows:

- **Decimal Input**

  If the user chooses decimal (1), they enter a decimal number. The program converts this number to binary, octal, and hexadecimal formats and displays the results.

- **Binary Input**

  If the user selects binary (2), they input a binary number. The program converts this number to decimal, octal, and hexadecimal formats.

- **Octal Input**

  For octal input (3), the user provides an octal number. The program converts it to decimal, binary, and hexadecimal formats.

- **Hexadecimal Input**

  If hexadecimal (4) is selected, the user inputs a hexadecimal number, which is then converted to decimal, binary, and octal formats.

### Code Example

**Conversion from Decimal to Other Bases:**

```python
if choice == 1:
    num = int(input("Enter a decimal number: "))
    print(f"Binary: {bin(num)[2:]}")
    print(f"Octal: {oct(num)[2:]}")
    print(f"Hexadecimal: {hex(num)[2:].upper()]}")
```

#### Conversion Functions:

- `bin(num)`: Converts a number to binary, prefixed with '0b'.
- `oct(num)`: Converts a number to octal, prefixed with '0o'.
- `hex(num)`: Converts a number to hexadecimal, prefixed with '0x'.
- **Prefix Removal**: `[2:]` removes the '0b', '0o', or '0x' prefix from the conversion results.

## Example

**Decimal to Other Bases:**

```
Choose the type of input number:
1. Decimal
2. Binary
3. Octal
4. Hexadecimal
Enter your choice (1-4): 1
Enter a decimal number: 255
Binary: 11111111
Octal: 377
Hexadecimal: FF
```

---
