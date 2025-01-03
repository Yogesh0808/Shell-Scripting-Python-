# Python Data Types 

Python has various data types:

- **String Data Type**  
  Example: `"Yogesh"`

- **Numeric Data Type**  
  1. **Integer**
  2. **Floating**

- **Mapping Data Type**  
  1. **List**
  2. **Tuple**

- **Boolean Data Type**  
  Possible values: `True` / `False`

*Note*: Python is a dynamically typed language, meaning there's no need to mention the data type like in Java or C++.

## Functions 

### Inbuilt Functions 

#### String Functions

1. **Length of a String**  
   To find the length of a string using `len()`:
   ```python
   str1 = "Hello"
   print(len(str1))  # Output: 5


2. **To Uppercase**
    To Covert the Character into UpperCase using `upper()`
    ```python
    str1 = "hello"
    print(str1.upper())  # Output: "HELLO"

3. **Convert to Lowercase**
    To convert all characters in a string to lowercase:
    ```python
       str1 = "HELLO"
       print(str1.lower())  # Output: "hello"


4. **Replace Substring**
    To replace part of the string with another substring:
    ```python

str1 = "Hello World"
print(str1.replace("World", "Python"))  # Output: "Hello Python"

5. **Find Substring**
    To find the index of a substring in the string:
    ```python
    str1 = "Hello"
    print(str1.find("l"))  # Output: 2

6. **Check if String Starts with Substring**
    To check if the string starts with a specific substring:
    ```python
    str1 = "Hello"
    print(str1.startswith("He"))  # Output: True

7. **Check if String Ends with Substring**
    To check if the string ends with a specific substring:
    ```python
    str1 = "Hello"
    print(str1.endswith("lo"))  # Output: True

8. **Split String**
    To split a string into a list of substrings:
    ```python
    str1 = "Hello World"
    print(str1.split())  # Output: ['Hello', 'World']

9. **Strip Whitespace**
    To remove leading and trailing whitespaces:
    ```python
    str1 = "  Hello World  "
    print(str1.strip())  # Output: "Hello World"

10. **Join List into String**
    To join a list of strings into one string:

    ```python
    words = ['Hello', 'World']
    print(" ".join(words))  # Output: "Hello World"


#### User Defined Functions
User-defined functions are created using the def keyword. Below are some examples:

**Basic Function Example**
- A function that prints "Hello, World!":

    ```python
    def greet():
        print("Hello, World!")

    greet()  # Output: "Hello, World!"

**Function with Arguments**
- A function that takes parameters and prints them:

    ```python
    def greet(name):
        print(f"Hello, {name}!")

    greet("Yogesh")  # Output: "Hello, Yogesh!"

**Function with Return Value**
- A function that takes two numbers, adds them, and returns the result:

    ```python
    def add(a, b):
        return a + b

    result = add(5, 3)
    print(result)  # Output: 8

**Function with Default Argument**
- A function with a default value for an argument:

    ```python
    def greet(name="Guest"):
        print(f"Hello, {name}!")

    greet("Yogesh")  # Output: "Hello, Yogesh!"
    greet()  # Output: "Hello, Guest!"

**Function with Variable Number of Arguments**
- A function that accepts any number of arguments using *args:

    ```python
    def display(*args):
        for arg in args:
            print(arg)

    display(1, 2, 3, "Hello")  # Output: 1 2 3 Hello

**Lambda Function**
- A small anonymous function using the lambda keyword:

    ```python
    add = lambda x, y: x + y
    print(add(5, 3))  # Output: 8

**Recursive Function**
- A function that calls itself (example for factorial calculation):

    ```python
    def factorial(n):
        if n == 0:
            return 1
        else:
            return n * factorial(n-1)

    print(factorial(5))  # Output: 120
