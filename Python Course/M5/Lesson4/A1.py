# Write a program to create a class with following variables and methods # 1. Private variable named privateVar that contains an integer value 
# 2. Create a private function privMeth that prints a message 
# 3. Create a function hello that prints the value of privateVar 
# 4. Create an object for the class and call all the functions.

# Step 1: Define a class named myClass.

# Step 2: Inside the class, create a private class variable __privateVar set to 27.

# Step 3: Define a private method __privMeth(self) that prints a short message.

# Step 4: Define a public method hello(self) that prints __privateVar's value using myClass.__privateVar.

# Step 5: Create an object foo of the myClass class.

# Step 6: Call foo.hello() - since hello() is a method inside the class, it reaches the private variable with no trouble.

# Step 7: Try reaching foo.__privMeth from outside the class - Python raises an AttributeError, proving a private method really can't be reached this way from outside.


class myClass:
    __privateVar=27

    def __privateMeth(self):
        print("I am a private method.")

    def hello(self):
        print("Printing a Private Variable",myClass.__privateVar)

foo=myClass()
foo.hello()
foo.__privateMeth