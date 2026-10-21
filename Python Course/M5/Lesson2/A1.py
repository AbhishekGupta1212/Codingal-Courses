# 1) Create a class named `IOString`.

# 2) Define the constructor method `__init__(self)`:
#    a) Initialize an instance variable `self.str1` with an empty string "".

# 3) Define a method `get_String(self)` to take input from the user:
#    a) Ask the user to enter a string.
#    b) Store the input in `self.str1`.

# 4) Define a method `print_String(self)` to display the string in uppercase:
#    a) Convert `self.str1` to uppercase using `.upper()`.
#    b) Print the result.

# 5) Create an object of the class `IOString` and store it in `str1`.

# 6) Call the method `get_String()` using the object to read input from the user.

# 7) Call the method `print_String()` using the object to print the uppercase string.


class IOString():
    def __init__(self):
        self.str1=""
    def get_String(self):
        self.str1=input("Enter a string: ")
    def print_String(self):
        print("Result is: ", self.str1.upper())


str1=IOString()

str1.get_String()
str1.print_String()