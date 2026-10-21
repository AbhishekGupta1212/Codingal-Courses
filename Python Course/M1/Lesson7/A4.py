# You will create an ASCII Value Checker that reveals the secret numeric code behind every character. Every letter, digit, and symbol on your keyboard has a unique number assigned to it in the ASCII system.

ASCII=input("Enter a character: ")

if len(ASCII)==1:
    print("The ASCII value of ", ASCII,"is ", ord(ASCII))
else:
    print("Enter a only a single character")