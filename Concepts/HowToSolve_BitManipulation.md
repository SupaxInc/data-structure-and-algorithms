# Cheat Sheet

## Binary Representation Table

| Decimal | Binary |
| --- | --- |
| 0 | 0000 |
| 1 | 0001 |
| 2 | 0010 |
| 3 | 0011 |
| 4 | 0100 |
| 5 | 0101 |
| 6 | 0110 |
| 7 | 0111 |
| 8 | 1000 |
| 9 | 1001 |
| 10 | 1010 |
| 11 | 1011 |
| 12 | 1100 |
| 13 | 1101 |
| 14 | 1110 |
| 15 | 1111 |

### Mentally Convert Number to Binary

1. **List Powers of 2**: Write down the powers of 2 in descending order that are less than or equal to your number. For instance, if you're converting the decimal number 13, list the powers of 2 like this: 8, 4, 2, 1 (since 2^3=8, 2^2=4, 2^1=2, and 2^0=1, and 8 is the largest power of 2 less than or equal to 13).
2. **Subtract Powers of 2**: Start from the largest power of 2 from your list and subtract it from your number if you can. Mark a 1 for each power you use and a 0 for each power you skip:
    - Can you subtract 8 (which is 2^3) from 13? Yes. 13−8=5, so you write down "1" for 2^3.
    - Move to the next lower power of 2, which is 4 (2^2). Can you subtract 4 from 5? Yes. 5−4=1, so you write down another "1" for 2^2.
    - Next is 2^1=2. Can you subtract 2 from 1? No, so you write down "0" for 2^1.
    - Finally, 2^0=1. Can you subtract 1 from 1? Yes, so you write down "1" for 2^0.
3. **Read the Binary Representation**: The binary representation of 13 is the series of 1s and 0s you wrote down: 1101.
4. **Visual Example for Number 13**
    - Powers of 2: 8, 4, 2, 1
    - Subtracting these from 13 in order:
        - 8? Yes (13-8=5) → 1
        - 4? Yes (5-4=1) → 1
        - 2? No (1-2 is not possible) → 0
        - 1? Yes (1-1=0) → 1
    - Binary Representation: 1101
5. **What if its more bits? E.g. 101000**
    1. Just do the same thing but add more powers of 2, 2^4, 2^5, etc.
        1. The rightmost digit (far right) is **`0`**, representing 2^0=1, but since the digit is **`0`**, it contributes **`0 * 1 = 0`**.
            
            20=1
            
        2. Moving left, the next digit is also **`0`**, representing 2^1=2, contributing **`0 * 2 = 0`**.
            
            21=2
            
        3. The third digit from the right is **`0`** again, representing 2^2=4, contributing **`0 * 4 = 0`**.
            
            22=4
            
        4. The fourth digit from the right is **`1`**, representing 2^3=8, contributing **`1 * 8 = 8`**.
            
            23=8
            
        5. The fifth digit from the right is **`0`**, representing 2^4=16, contributing **`0 * 16 = 0`**.
            
            24=16
            
        6. The leftmost digit is **`1`**, representing ^25=32, contributing **`1 * 32 = 32`**.
            
            25=32
            
    
    Now, add up all the contributions: **`0 + 0 + 0 + 8 + 0 + 32 = 40`**.
    

### Mentally Convert Binary to Number

1. **Write Down the Powers of 2**: Starting from the right (the least significant bit), write down the powers of 2 for each digit in the binary number. For a binary number like **`1101`**, you would write down the powers corresponding to each digit's position, starting with 2020 on the right:
    
    ```
    1    1    0    1
    2^3  2^2  2^1  2^0
    ```
    
2. **Multiply Each Binary Digit by Its Corresponding Power of 2**: For each digit in the binary number, if the digit is 1, you take the corresponding power of 2; if it's 0, you ignore it. Continuing with the binary **`1101`**:
    - For the first **`1`** (from the left), you have 2^3=8.
        
        2^3=8
        
    - For the second **`1`**, 2^2=4.
        
        2^2=4
        
    - The **`0`** contributes nothing, so you skip 2^1.
        
        2^1
        
    - For the last **`1`**, 2^0=1.
        
        2^0=1
        
3. **Add the Results Together**: Sum the values you've calculated for each **`1`** digit:
    - 8+4+0+1=138+4+0+1=13.

### Converting in Python

- **Binary Literals**: Start with **`0b`**, e.g., **`0b101`** is **`5`** in decimal.
- **Convert to Binary**: **`bin(x)`** returns the binary representation of **`x`** as a string.
- **Convert to Integer**: **`int('binary_string', 2)`** converts a binary string to an integer.

## Bitwise Operations

1. **AND (`&`)**:
    - Binary Operation: **`a & b`**
    - Effect: Each bit of the output is **`1`** if the corresponding bits of **`a`** and **`b`** are both **`1`**, otherwise **`0`**.
    - Example: **`1010 & 1100 = 1000`**
2. **OR (`|`)**:
    - Binary Operation: **`a | b`**
    - Effect: Each bit of the output is **`1`** if at least one of the corresponding bits of **`a`** or **`b`** is **`1`**.
    - Example: **`1010 | 1100 = 1110`**
3. **XOR (`^`)**:
    - Binary Operation: **`a ^ b`**
    - Effect: Each bit of the output is **`1`** if the corresponding bits of **`a`** and **`b`** are different, otherwise **`0`**.
    - Example: **`1010 ^ 1100 = 0110`**
4. **NOT (`~`)**:
    - Unary Operation: **`~a`**
    - Effect: Inverts the bits of **`a`** (0 becomes 1, and 1 becomes 0).
    - Example: **`~1010 = 0101`** (in reality, due to two's complement representation, it will also consider the sign bit)
5. **Left Shift (`<<`)**:
    - Binary Operation: **`a << b`**
    - Effect: Shifts the bits of **`a`** to the left by **`b`** positions, filling the new rightmost bits with **`0`**.
    - Example: **`1010 << 2 = 101000`**
6. **Right Shift (`>>`)**:
    - Binary Operation: **`a >> b`**
    - Effect: Shifts the bits of **`a`** to the right by **`b`** positions. For signed numbers, the new leftmost bits depend on the sign bit.
    - Example: **`1010 >> 2 = 0010`**
    

## Common Bit Manipulation Tricks

- **Setting a Bit**: Set the **`i`**th bit of **`a`** to **`1`**: **`a | (1 << i)`**
- **Clearing a Bit**: Set the **`i`**th bit of **`a`** to **`0`**: **`a & ~(1 << i)`**
- **Toggling a Bit**: Toggle the **`i`**th bit of **`a`**: **`a ^ (1 << i)`**
- **Checking a Bit**: Check if the **`i`**th bit of **`a`** is set (**`1`**): **`(a & (1 << i)) != 0`**
- **Stripping the Lowest Set Bit**: **`a & (a - 1)`** turns off the lowest set bit of **`a`**
- **Get the Lowest Set Bit**: **`a & -a`** isolates the lowest set bit of **`a`**
- **Get Most Significant Bit (MSB) for 32-bit Integer**: **`1 << (31 - x.bit_length())`** if **`x != 0`** else **`0`**

### Python Examples

```python
# Set the 3rd bit of x
x = 0b1010  # 10 in decimal
x |= (1 << 3)  # x = 0b11010

# Clear the 2nd bit of x
x &= ~(1 << 2)  # x = 0b11000

# Toggle the 1st bit of x
x ^= (1 << 1)  # x = 0b11010

# Check if the 4th bit of x is set
is_set = (x & (1 << 4)) != 0  # False
```

## Useful Concepts

- **Two's Complement**: Negative numbers are represented as the two's complement of their absolute values, which is why **`~a`** is not just a simple bit inversion from a human perspective.
- **Bit Masking**: Using bitwise operations to manipulate specific bits within a number, useful for compactly storing and retrieving several boolean flags within a single integer.