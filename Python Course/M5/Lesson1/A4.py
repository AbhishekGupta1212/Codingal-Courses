# Write a program to create a dog class with one class variable and two instance variables, and display the details of dogs of two different breeds.

class dog:
    sound="bark"
    def __init__(self,name,breed):
        self.name=name
        self.breed=breed

Luu=dog("Loo","Great Dane")
Brick=dog("Brick","Tibetan Mastiff")

print(f"{Luu.name} is a {Luu.breed}, whenever he sees a stranger he {Luu.sound}s.")
print(f"{Brick.name} is a {Brick.breed}, whenever he sees a stranger he {Brick.sound}s.")