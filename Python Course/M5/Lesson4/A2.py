# Write a program to create a class Computer with a private attribute max_price and methods sell(to display) the selling price and setmaxprice(change the private attribute max_price). Now create an object for the class Computer. Try changing the value of max price and use the sell function to display the updated price. Use a setter function to update the value and again display the price.

# Step 1: Define a class named Computer.

# Step 2: Inside __init__(self), set a private instance variable self.__maxprice to 900.

# Step 3: Define a method sell(self) that prints the current selling price using an f-string.

# Step 4: Define a setter method setMaxPrice(self, price) that updates self.__maxprice to the new price.

# Step 5: Create an object c and call c.sell() - it prints 900.

# Step 6: Try setting c.__maxprice = 1000 directly, then call c.sell() again - it still prints 900, since this only created a new, separate attribute instead of touching the real private value.

# Step 7: Call c.setMaxPrice(1000), then call c.sell() one more time - it now prints 1000, since the setter actually reached the real private variable.

class Computer:

    def __init__(self):
        self.__maxprice=900


    

    def sell(self):
        print(f"Current selling price: {self.__maxprice} ")

    def setMaxPrice(self,price):
        self.__maxprice=price


c=Computer()
c.sell()

c.__maxprice=1000
c.sell()

c.setMaxPrice(1000)
c.sell()