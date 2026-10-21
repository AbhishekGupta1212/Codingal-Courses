# Write a program to check the age entered by the user is correct or not. If there is some error in the value of age entered. And check that the age entered by the user is even or odd, use exception handling to handle the error.

try:
    age = int(input("Enter your age: "))
    if age < 0:
        raise ValueError("Age cannot be negative.")
    elif age % 2 == 0:
        print("The age entered is even.")
    else:
        print("The age entered is odd.")
except ValueError as e:
    print("Error:", e)