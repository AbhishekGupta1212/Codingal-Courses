# A My Family Trait Tree program that builds a parent class holding shared family traits, a child class that inherits and adds its own details, overrides a method to show everything together, and checks the family connection with issubclass().

# HOW IT WORKS

# Step 1: Create a parent class called FamilyMember that stores shared traits like eye colour and height.

# Step 2: Create a child class called Kid that inherits from FamilyMember.

# Step 3: Give Kid its own details, then use super().__init__() to pull in the parent's traits too.

# Step 4: Override show_traits() inside Kid to display the kid's own details plus the inherited ones.

# Step 5: Add a brand new method inside Kid that only the child class has.

# Step 6: Create a Kid object and call both the overridden method and the new method.

# Step 7: Check with issubclass() whether Kid truly is a subclass of FamilyMember.


class FamilyMember:
    def __init__(self,height,eye_color):
        self.height=height
        self.eye_color=eye_color

    def show_traits(self):
        print("Eye Color: ",self.eye_color)
        print("Height: ",self.height)


class Kid(FamilyMember):
    def __init__(self, height, eye_color,name,age):
        self.name=name
        self.age=age
        super().__init__(height, eye_color)

    def show_traits(self):
        print("Name:",self.name)
        print("Age",self.age)
        super().show_traits()

    def favorite_food(self,food):
        print(self.name,"likes to have:",food)


child=Kid(140,"green","Ronny",12)
child.favorite_food("Fritter")

print("Is Kid subclass of FamilyMember?", issubclass(Kid,FamilyMember))