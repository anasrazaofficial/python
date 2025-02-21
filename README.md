# python

## Basic

- **print(val1)**: is used to print
- **input(message)**: is used to take input

> [Code](./basic.py)

## Type Conversion

- **type(var/val)**: shows the data type
- **int(val)**: converts value to integer
- **str(val)**: converts value to string
- **float(val)**: converts value to float (decimal)

> [Code](./typeConversion.py)

## Strings

- **var[0]**: to get 0 (zero) index of string
- **var[-1]**: to get indexes from last of the string
- **var[0:3]**: slices from 0 index and 3 characters
- **var[3:]**: slices from 3 index till end
- **var[:3]**: slices from 0 index and 3 characters
- **Template literals**: `f"My name is {firstName} {lastName}"`
    - firstName = "Anas"
    - lastName = "Raza"
    - Output = "My name is Anas Raza"
    - _Note: **f** is used before the strings_

### String Methods

- **len(string)**: Shows the length of the string
- **string.upper()**: Converts all the characters to uppercase
- **string.lower()**: Converts all the characters to lowercase
- **course.find(char)**: Gives the index of the first occurrence of the character. It is case-sensitive
- **string.replace(old, new)**: Replaces all the `old`s with `new`s
    - **in**: Returns boolean for if the value is in the value or not
        ```python
          course= "Python"
          print("on" in course) # True
          print("On" in course) # False

> [Code](./strings.py)