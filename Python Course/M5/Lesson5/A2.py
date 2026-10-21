from abc import ABC,abstractmethod
#Write a program to implement abstraction on animal class (base class). The abstract method will be move will display what subclasses can do. Subclasses can be something like - Human, Dog. 

# Step 1: Import ABC and abstractmethod from Python's abc module.

# Step 2: Define an abstract base class Animal that inherits from ABC.

# Step 3: Inside Animal, define an abstract method move(self) using pass as a placeholder.

# Step 4: Define a subclass Human that overrides move() to print "I can walk and run".

# Step 5: Define a subclass Snake that overrides move() to print "I can crawl".

# Step 6: Define a subclass Dog that overrides move() to print "I can bark".

# Step 7: Define a subclass Lion that overrides move() to print "I can roar".

# Step 8: Create one object of each subclass and call .move() on each - every object runs its own version of the method.

class Animal(ABC):

    @abstractmethod
    def move(self):
        pass

class Human(Animal):
    def move(self):
         print("I can walk and run.")

class Snake(Animal):
    def move(self):
        print("I can crawl.")

class Dog(Animal):

    def move(self):
        print("I can bark.")

class Lion(Animal):

    def move(self):
        print("I can roar.")

F=Human()
F.move()

S=Snake()
S.move()

D=Dog()
D.move()

L=Lion()
L.move()