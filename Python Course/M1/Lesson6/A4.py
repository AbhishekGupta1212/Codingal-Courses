# Assignment: Checking Alphabets
# Create a program to check if the given character is an alphabet or not.
 
ch=input("Enter a character: ")

if('a'<= ch <= 'z') or('A'<=ch<='Z'):
    print("It is an alphabet")
else:
    print("Not an alphabet")