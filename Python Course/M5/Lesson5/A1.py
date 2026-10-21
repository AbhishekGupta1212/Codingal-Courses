from abc import ABC, abstractmethod

# Write a program to create a base class that consists of two functions - one to display a value, and another function is an abstract method. Next, create a subclass that consists of a method similar to the abstract method. Finally, showcase how Abstraction is being implemented in this example.

# Step 1: Import ABC and abstractmethod from Python's abc module.

# Step 2: Define an abstract base class Absclass that inherits from ABC.

# Step 3: Inside Absclass, define a normal method print(self, x) that prints the passed-in value.

# Step 4: Define an abstract method task(self) using the @abstractmethod decorator.

# Step 5: Define a subclass test_class that inherits from Absclass and implements task(self), printing its own message.

# Step 6: Create an object test_obj of test_class - this works because task() has been properly implemented.

# Step 7: Call test_obj.task() to run the overridden method, then call test_obj.print(100) to run the inherited normal method.



class Absclass(ABC):

     def print(self,x):
          print("Value Passed",x)

     @abstractmethod
     def task(self):
          print("Inside Absclass task.")

class test_class(Absclass):
     def task(self):
          print("Inside task class.")

test_obj=test_class()
test_obj.task()
test_obj.print(100)

