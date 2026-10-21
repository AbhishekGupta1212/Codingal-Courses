# Write a program to create a class Point that consists of a constructor to set coordinates equal to x and y. Also, it consists of a function that returns the coordinates in Point format. Create an object passing the coordinates and print the Point.

# Step 1: Define a class named Point.

# Step 2: Define __init__(self, x, y) and store both values onto self.x and self.y.

# Step 3: Define the special function __str__(self), returning an f-string formatted as "(x, y)".

# Step 4: Create an object p1 by calling Point(2, 3).

# Step 5: Call print(p1) - Python automatically calls __str__ behind the scenes and prints its returned text, showing (2, 3).

class Point:

    def __init__(self,x,y):
        self.x=x
        self.y=y

    def __str__(self):
        return f"{self.x,self.y}"


p1=Point(2,3)
print(p1)