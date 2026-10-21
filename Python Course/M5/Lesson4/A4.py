# You will build an Account PIN Safety Checker using Python. You will create private account data, test how private attributes behave outside the class, update private data safely using a setter method, and use the __str__ special function to control how an object is displayed with print().


# Step 1: Create the Account Class Create a class called Account. This class will store account information and include methods to manage the PIN safely.

# Step 2: Add the __init__() Method Inside __init__(), store owner as a regular attribute and __pin as a private attribute. The double underscore shows that the PIN should not be changed directly from outside the class.

# Step 3: Access Private Data Inside the Class Create show_pin_status() and check_pin(). These methods can use the private PIN safely because they are inside the class.

# Step 4: Create a Setter Method Create set_pin(new_pin). Use an if statement to allow only a four-digit PIN. If the value is valid, update the private PIN. Otherwise, print an error message.

# Step 5: Add the __str__() Special Function Create __str__() to return a clear text message when the object is printed with print(my_account).

# Step 6: Create and Print the Object Create my_account using an owner name and PIN. Then print the object to check that __str__() is working.

# Step 7: Test Direct Outside Update Try assigning my_account.__pin = "9999". Then check both 9999 and 1234 to see that the real private PIN did not change through direct outside assignment.

# Step 8: Update the PIN Safely Use my_account.set_pin("9999") to update the private PIN correctly. Then check the new PIN to confirm that the setter worked.

# Step 9: Run and Explore Run the program and change the owner name, starting PIN, and new PIN. Try invalid values such as "99" or "abcd" to test the setter validation.


class Account:

    def __init__(self,owner_name,pin):
        self.owner_name=owner_name
        self.__pin=pin

    def show_pin_status(self):
        print("Account Holder's name: ",self.owner_name)
        print("PIN safe inside the class.")


    def set_pin(self,new_pin):
        if len(new_pin)==4 and new_pin.isdigit():
            self.__pin=new_pin
            print("Requirements matched for pin creation.")
        else:
            print("Error, keep the pin of 4-digit only.")

    def check_pin(self,pin):
        if pin==self.__pin:
            print("Authorized.")
        else:
            print("Unauthorized.")

    def __str__(self):
        return "Account Holder's Name:"+self.owner_name


account1=Account("Rin","5874")
account1.set_pin("9621")
account1.show_pin_status()

account1.check_pin("9621")
account1.set_pin("1456")