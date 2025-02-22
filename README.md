# python

## Basic

- **print(val1)**: is used to print
- **input(message)**: is used to take input
- Logical operators are **and** for `&&`, **or** for `||`, and **not** for `!`
- **range(start, end, step)**
    - If 1 param then run till `start`
    - If 2 params then runs from `start` till `end`
    - If 3 params then runs from `start` till `end` with `step`
- **Unpacking**: Extracting the elements of a collection into variables

> [Code](./basic.py), [Range](./loops.py), [Unpacking](./unpacking.py)

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

## Math

- **a // b**: Divides and gives the before point value (`3.333` -> `3`)
- **round(num)**: Rounds off the value
- **abs(num)**: Makes value absolute (positive)

> [Code](math.py)

## Lists

- **max(list)**: Finds the largest number from the list
- **list.append(element)**: Adds the element just like push
- **list.pop()**: Removes the last index
- **list.insert(element, index)**: Insert the element at given index
- **list.remove(element)**: Removes the first given element occurrence
- **element in list**: Returns the boolean if an element is in the list
- **list.index(element)**: Returns the index of that element
- **list.count(element)**: Counts the element occurrence
- **list2 = list.copy()**: Copies the list
- **list.sort()**: Sorts the list
- **list.reverse()**: Reverses the list
- **list.clear()**: Empty the list

> [Code](./list.py)

## Tuples

Similar to lists but immutable (unchangeable). Methods:

- **list.index(element)**: Returns the index of that element
- **list.count(element)**: Counts the element occurrence

> [Code](./tuples.py)

## OOP

### Class and Constructor

- **def __init__(self, params...)**: Self is passed as `this`
- `self` is also passed in every function definition but not while calling

> [Code](./OOP/Classes.py)

### Inheritance

- Inherits another class with parameters, `class Child(Parent):`
- **pass**: When you do not want anything in a child class

```python
class Parent:
    def func(self):
        print("Hello world")


class Dog(Parent):
    pass
```

> [Code](./OOP/Inheritance.py)