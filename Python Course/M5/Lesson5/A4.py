from abc import ABC,abstractmethod

# You will build a Smart Device Command Center using Python. You will use abstraction to create a common smart device structure, create an abstract class with an abstract method, override methods in different device classes, and use polymorphism with shared method names.

# Step 1: Import the Abstraction Tools Create a new Python file. Import ABC and abstractmethod from the abc module so you can build an abstract class.

# Step 2: Create the Abstract Class Create SmartDevice(ABC). Add a common method called show_device() and an abstract method called turn_on().

# Step 3: Add the Abstract Method Use @abstractmethod above turn_on(). Keep pass inside it because each child class will write its own version of this method.

# Step 4: Override the Method in Subclasses Create SmartLight, SmartFan, and SmartSpeaker. Each class should inherit from SmartDevice and define its own turn_on() method.

# Step 5: Create Objects and Call Methods Create objects for the light, fan, and speaker. Use show_device() to display the device name and turn_on() to run each device-specific action.

# Step 6: Show Polymorphism Without Inheritance Create SecurityCamera and DoorLock. These classes do not inherit from SmartDevice, but both use the same method name, check_status().

# Step 7: Use a Shared Interface Place the SecurityCamera and DoorLock objects inside a list. Loop through the list and call check_status() on each object.

# Step 8: Run and Explore Run the program and read the output. Try adding another smart device class, such as SmartTV, and give it its own turn_on() method.

class SmartDevice(ABC):
    def show_device(self,name):
        print("Device Name:", name)

    @abstractmethod
    def turn_on(self):
        pass

class SmartLight(SmartDevice):
    def turn_on(self):
        print("Smart Light is ON.")

class SmartFan(SmartDevice):
    def turn_on(self):
        print("Smart Fan is ON.")

class SmartSpeaker(SmartDevice):
    def turn_on(self):
        print("Smart Speaker is ON.")

light=SmartLight()
fan=SmartFan()
speaker=SmartSpeaker()


light.show_device("Hall Light")
light.turn_on()

fan.show_device("Ceiling Fan")
fan.turn_on()

speaker.show_device("JBL Speaker")
speaker.turn_on()


class SecurityCamera:
    def check_status(self):
        print("Camera is working.")

class DoorLock:
    def check_status(self):
        print("Lock secured.")

lock=DoorLock()
camera=SecurityCamera()

security=[lock,camera]

for device in security:
    device.check_status()
