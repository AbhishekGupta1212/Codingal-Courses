# In this assignment, you will build a Vehicle Type Builder using Python. You will create a parent vehicle class, build a child car class, inherit parent features, override a method, use super(), and check the inheritance relationship with issubclass().

class Vehicle:
    def __init__(self,fuel_type,seats):
        self.fuel_type=fuel_type
        self.seats=seats

    def features(self):
        print("Fuel Type:",self.fuel_type)
        print("Passenger Capacity:",self.seats)


class Car(Vehicle):
    def __init__(self,color,transmission_type, fuel_type, seats):
        self.color=color
        self.transmission_type=transmission_type
        super().__init__(fuel_type, seats)


    def features(self):
        print("Car's color is:",self.color)
        print("Car's transmission is:",self.transmission_type)
        super().features()


SUV=Car("Light Gray","Manual","Diesel",7)
SUV.features()
print("Is Child a subclass of Parent?", issubclass(Car,Vehicle))

        